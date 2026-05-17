# Hospital Management API

## Bulk Upload Hospitals

Creates hospitals from a CSV file, groups them under a generated batch ID, and activates the created batch after upload.

### Endpoint

```http
POST /hospitals/bulk
```

### Request

Send a multipart form-data request with one CSV file field named `file`.

```bash
curl -X POST http://localhost:8000/hospitals/bulk \
  -F "file=@hospitals.csv"
```

### CSV Format

The CSV must include these headers:

```csv
name,address,phone
Apollo Hospital,Bangalore,9876543210
Wellness Clinic,Surat,
```

Fields:

| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Hospital name. Blank values fail row validation. |
| `address` | Yes | Hospital address. Blank values fail row validation. |
| `phone` | No | Optional phone number. Blank values are accepted. |

Rules:

- Only `.csv` files are accepted.
- Maximum allowed rows: `20`.
- Header names are normalized to lowercase and trimmed.
- Each valid hospital is first created as inactive with a shared `creation_batch_id`.
- After the CSV is processed, the endpoint activates hospitals in that batch.

### Success Response

```json
{
  "status": "completed",
  "batch_id": "f81b3f76-70d2-4b77-9dbf-bd46b3d97325",
  "total_hospitals": 2,
  "processed_hospitals": 2,
  "failed_hospitals": 0,
  "processing_time_seconds": 1.42,
  "message": "Bulk hospital processing completed",
  "hospitals": [
    {
      "creation_batch_id": "f81b3f76-70d2-4b77-9dbf-bd46b3d97325",
      "name": "Apollo Hospital",
      "address": "Bangalore",
      "phone": "9876543210",
      "active": false,
      "id": 10
    }
  ]
}
```

### Status Values

| Status | Meaning |
| --- | --- |
| `completed` | All valid rows were created successfully. |
| `completed_with_errors` | Some rows failed, but at least one hospital was created. |
| `failed` | No hospitals were created, or required CSV columns are missing. |

### Error Cases

Non-CSV upload:

```json
{
  "detail": "Only CSV files allowed"
}
```

More than 20 rows:

```json
{
  "status": "Please upload less than or equal to 20 records"
}
```

Missing required columns:

```json
{
  "batch_id": "f81b3f76-70d2-4b77-9dbf-bd46b3d97325",
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
      "row": null,
      "reason": "Missing columns: address"
    }
  ]
}
```

Row validation failures are tracked internally during processing. A row fails when `name` or `address` is blank.
