import csv
import io
from uuid import uuid4
import uuid
from services.exceptions import CSVLimit
from services.hospital_api import create_hospital, activate_batch
from services.models import HospitalCreateRequest


REQUIRED_COLUMNS = {"name", "address"}


def _clean_optional_value(value):
    """
    Normalize an optional CSV field value.

    Converts `None`, empty strings, and whitespace-only strings to `None`.
    Non-empty values are returned as stripped strings.
    """
    if value is None:
        return None

    value = str(value).strip()
    return value or None


def _read_csv_rows(file):
    """
    Read an uploaded CSV file into dictionaries.

    The file pointer is reset before reading. Byte content is decoded as
    UTF-8 with BOM support, and header names are trimmed and lowercased.

    Returns:
        A tuple containing the CSV rows and the normalized column names.
    """
    file.file.seek(0)
    content = file.file.read()

    if isinstance(content, bytes):
        content = content.decode("utf-8-sig")

    reader = csv.DictReader(io.StringIO(content))
    if not reader.fieldnames:
        return [], set()

    reader.fieldnames = [
        field.strip().lower() if field else field
        for field in reader.fieldnames
    ]
    return list(reader), set(reader.fieldnames)


async def process_csv(file):
    """
    Process a hospital CSV upload and create hospitals in the downstream API.

    The CSV must contain `name` and `address` columns. The `phone` column is
    optional. A generated batch ID is attached to every valid hospital request,
    and each successful API response is added to the returned hospital list.

    Args:
        file: FastAPI UploadFile containing CSV data.

    Returns:
        A dictionary with processing status, batch ID, total row count,
        processed count, failed count, placeholder processing time, message,
        and created hospital records.

    Raises:
        CSVLimit: If the uploaded CSV contains more than 20 rows.
    """

    rows, columns = _read_csv_rows(file)

    if len(rows) > 20:
        raise CSVLimit

    missing_columns = REQUIRED_COLUMNS - columns
    if missing_columns:
        return {
            "batch_id": str(uuid4()),
            "status": "failed",
            "message": "CSV is missing required columns",
            "progress": {
                "total": 0,
                "processed": 0,
                "success": 0,
                "failed": 0,
                "percentage": 0
            },
            "errors": [
                {
                    "row": None,
                    "reason": f"Missing columns: {', '.join(sorted(missing_columns))}"
                }
            ]
        }

    batch_id = str(uuid4())

    total = len(rows)
    processed = 0
    success = 0
    failed = 0
    errors = []
    hospitals = []
    time_to_comeplete = 250  # TODA

    for index, row in enumerate(rows, start=1):
        processed += 1
        name = _clean_optional_value(row.get("name"))
        address = _clean_optional_value(row.get("address"))
        phone = _clean_optional_value(row.get("phone"))

        hospital_data = {
            "creation_batch_id": batch_id,
            "name": name,
            "address": address,
            "phone": phone,
            "active": False
        }
        if not name or not address:
            failed += 1
            errors.append({
                "row": index,
                "reason": "name and address are required"
            })
            continue
        try:
            request = HospitalCreateRequest(
                name=name,
                address=address,
                phone=phone,
                creation_batch_id=batch_id
            )
            response = await create_hospital(request)
            if response:
                success += 1
            hospital_data['id'] = response.json().get('id')
            hospitals.append(hospital_data)
        except Exception as e:
            failed += 1
            errors.append({
                "row": index,
                "reason": str(e)
            })

    status = "completed"
    if failed and success:
        status = "completed_with_errors"
    elif failed and not success:
        status = "failed"

    return {
        "status": status,
        "batch_id": batch_id,
        "total_hospitals": total,
        "processed_hospitals": total,
        "failed_hospitals": len(errors),
        "processing_time_seconds": time_to_comeplete,
        "message": "Bulk hospital processing completed",
        "hospitals": hospitals,
    }


async def process_batch(batch_id: uuid.UUID):
    """
    Activate all hospitals created under a batch ID.

    Args:
        batch_id: UUID of the hospital creation batch to activate.

    Returns:
        Parsed JSON response from the downstream batch activation API.
    """

    response = await activate_batch(batch_id=batch_id)
    data = response.json()

    return data
