import httpx
import uuid

from services.models import HospitalCreateRequest


HOSPITAL_API_URL = "https://hospital-directory.onrender.com/"


async def create_hospital(data: HospitalCreateRequest):
    url = f"{HOSPITAL_API_URL.rstrip('/')}/hospitals/"

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            url,
            json=data.to_payload()
        )

        if response.status_code in (200, 201):
            return response

        raise Exception(
            f"Hospital API failed with {response.status_code}: {response.text}"
        )
        

async def activate_batch(batch_id: uuid.uuid4):
    url = f"{HOSPITAL_API_URL.rstrip('/')}/hospitals/batch/{batch_id}/activate"

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.patch(
            url,
            
        )
        print(response.status_code, response.json())
        if response.status_code in (200, 201):
            return response

        raise Exception(
            f"Hospital API failed with {response.status_code}: {response.text}"
        )        
