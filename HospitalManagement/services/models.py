from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HospitalCreateRequest:
    """
    Request model for creating a hospital through the downstream API.

    Attributes:
        name: Hospital name.
        address: Hospital address.
        phone: Optional hospital phone number.
        creation_batch_id: Optional batch UUID used to group bulk uploads.
    """
    name: str
    address: str
    phone: Optional[str] = None
    creation_batch_id: Optional[str] = None

    def to_payload(self):
        """
        Convert the request model to an API payload.

        Optional fields are included only when they have non-empty values.
        """
        payload = {
            "name": self.name,
            "address": self.address,
        }

        if self.phone:
            payload["phone"] = self.phone

        if self.creation_batch_id:
            payload["creation_batch_id"] = self.creation_batch_id

        return payload
