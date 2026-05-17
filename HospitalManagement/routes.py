from datetime import datetime, timezone

from fastapi import APIRouter, UploadFile, File, HTTPException
from services.exceptions import CSVLimit
from fastapi.responses import JSONResponse
from services.csv_service import process_csv, process_batch


hospital_router = APIRouter(prefix="/hospitals")


@hospital_router.post("/bulk")
async def bulk_upload(file: UploadFile = File(...)):
    """
    Upload a CSV file and create hospitals in bulk.

    The request must be sent as multipart form data with a CSV file in the
    `file` field. The CSV should include `name`, `address`, and optional
    `phone` columns. Each valid row is created under a generated batch ID,
    then the created batch is activated through the downstream hospital API.

    Returns a processing summary containing the batch ID, total hospitals,
    activated hospital count, failed hospital count, processing time, and the
    created hospital records. Raises a 400 response when the uploaded file is
    not a CSV or when the CSV exceeds the allowed row limit.
    """
    try:
        if not file.filename or not file.filename.lower().endswith(".csv"):
            raise HTTPException(
                status_code=400, detail="Only CSV files allowed")
        start_time = datetime.now(timezone.utc)
        result = await process_csv(file)
        final_response = await process_batch(result['batch_id'])
        result["processed_hospitals"] = final_response['activated_count']
        end_time = datetime.now(timezone.utc)
        seconds_elapsed = (end_time - start_time).total_seconds()
        result['processing_time_seconds'] = seconds_elapsed
        return result
    except CSVLimit as e:
        return JSONResponse(
            status_code=400,
            content={
                "status": str(e)
            }
        )
