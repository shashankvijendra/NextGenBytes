import io
import sys
import types
import unittest
import uuid


if "httpx" not in sys.modules:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object)

from services import csv_service
from services.exceptions import CSVLimit
from services.models import HospitalCreateRequest


class FakeUploadFile:
    def __init__(self, content):
        self.file = io.StringIO(content)


class FakeResponse:
    def __init__(self, data):
        self._data = data

    def json(self):
        return self._data

    def __bool__(self):
        return True


class CsvServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.original_create_hospital = csv_service.create_hospital
        self.original_activate_batch = csv_service.activate_batch
        self.original_uuid4 = csv_service.uuid4

    def tearDown(self):
        csv_service.create_hospital = self.original_create_hospital
        csv_service.activate_batch = self.original_activate_batch
        csv_service.uuid4 = self.original_uuid4

    def test_clean_optional_value_normalizes_blank_values(self):
        self.assertIsNone(csv_service._clean_optional_value(None))
        self.assertIsNone(csv_service._clean_optional_value(""))
        self.assertIsNone(csv_service._clean_optional_value("   "))
        self.assertEqual(csv_service._clean_optional_value(" 12345 "), "12345")

    def test_read_csv_rows_normalizes_headers(self):
        file = FakeUploadFile(" Name , Address , Phone \nA Hospital,Main Road,123\n")

        rows, columns = csv_service._read_csv_rows(file)

        self.assertEqual(columns, {"name", "address", "phone"})
        self.assertEqual(rows[0]["name"], "A Hospital")
        self.assertEqual(rows[0]["address"], "Main Road")
        self.assertEqual(rows[0]["phone"], "123")

    async def test_process_csv_creates_hospitals_with_batch_id(self):
        batch_id = uuid.UUID("a7c9d2f1-3e84-4b6a-91fd-2c5e7f8a9b10")
        csv_service.uuid4 = lambda: batch_id
        created_requests = []

        async def fake_create_hospital(request):
            created_requests.append(request)
            return FakeResponse({"id": len(created_requests)})

        csv_service.create_hospital = fake_create_hospital
        file = FakeUploadFile(
            "name,address,phone\n"
            "City Hospital,Main Road,12345\n"
            "Care Clinic,Second Street,\n"
        )

        result = await csv_service.process_csv(file)

        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["batch_id"], str(batch_id))
        self.assertEqual(result["total_hospitals"], 2)
        self.assertEqual(result["processed_hospitals"], 2)
        self.assertEqual(result["failed_hospitals"], 0)
        self.assertEqual([hospital["id"] for hospital in result["hospitals"]], [1, 2])
        self.assertEqual(len(created_requests), 2)
        self.assertEqual(created_requests[0].phone, "12345")
        self.assertIsNone(created_requests[1].phone)
        self.assertEqual(created_requests[0].creation_batch_id, str(batch_id))

    async def test_process_csv_returns_failed_for_missing_required_columns(self):
        file = FakeUploadFile("name,phone\nCity Hospital,12345\n")

        result = await csv_service.process_csv(file)

        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["message"], "CSV is missing required columns")
        self.assertEqual(result["progress"]["total"], 0)
        self.assertEqual(result["errors"][0]["reason"], "Missing columns: address")

    async def test_process_csv_raises_csv_limit_for_more_than_20_rows(self):
        rows = ["name,address,phone"]
        rows.extend(f"Hospital {index},Address {index}," for index in range(21))
        file = FakeUploadFile("\n".join(rows))

        with self.assertRaises(CSVLimit):
            await csv_service.process_csv(file)

    async def test_process_csv_marks_invalid_rows_failed(self):
        async def fake_create_hospital(request):
            return FakeResponse({"id": 10})

        csv_service.create_hospital = fake_create_hospital
        file = FakeUploadFile(
            "name,address,phone\n"
            ",Missing Name Address,12345\n"
            "Valid Hospital,Main Road,\n"
        )

        result = await csv_service.process_csv(file)

        self.assertEqual(result["status"], "completed_with_errors")
        self.assertEqual(result["failed_hospitals"], 1)
        self.assertEqual(len(result["hospitals"]), 1)
        self.assertEqual(result["hospitals"][0]["name"], "Valid Hospital")

    async def test_process_batch_returns_activation_json(self):
        async def fake_activate_batch(batch_id):
            return FakeResponse({"activated_count": 2, "batch_id": str(batch_id)})

        csv_service.activate_batch = fake_activate_batch
        batch_id = uuid.UUID("a7c9d2f1-3e84-4b6a-91fd-2c5e7f8a9b10")

        result = await csv_service.process_batch(batch_id)

        self.assertEqual(result["activated_count"], 2)
        self.assertEqual(result["batch_id"], str(batch_id))


class HospitalCreateRequestTest(unittest.TestCase):
    def test_to_payload_omits_empty_optional_fields(self):
        request = HospitalCreateRequest(name="A Hospital", address="Main Road")

        self.assertEqual(
            request.to_payload(),
            {"name": "A Hospital", "address": "Main Road"}
        )

    def test_to_payload_includes_optional_fields(self):
        request = HospitalCreateRequest(
            name="A Hospital",
            address="Main Road",
            phone="12345",
            creation_batch_id="a7c9d2f1-3e84-4b6a-91fd-2c5e7f8a9b10"
        )

        self.assertEqual(
            request.to_payload(),
            {
                "name": "A Hospital",
                "address": "Main Road",
                "phone": "12345",
                "creation_batch_id": "a7c9d2f1-3e84-4b6a-91fd-2c5e7f8a9b10"
            }
        )


if __name__ == "__main__":
    unittest.main()
