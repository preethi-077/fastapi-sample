from pydantic import BaseModel, EmailStr, constr, validator
from app.models.client import ClientTypeEnum
import re

# Shared fields
class ClientBase(BaseModel):
    name: constr(min_length=3, max_length=50)   # Name must be 3–50 chars
    email: EmailStr                             # Valid email format
    client_type: ClientTypeEnum                 # Retail / Corporate
    phone: constr(min_length=10, max_length=15) # Phone must be 10–15 chars

    # Custom validator for phone numbers
    @validator("phone")
    def validate_phone(cls, value):
        pattern = re.compile(r"^[0-9]{10,15}$")  # Only digits, length 10–15
        if not pattern.match(value):
            raise ValueError("Phone must contain only digits (10–15 characters)")
        return value

# For creating a new client
class ClientCreate(ClientBase):
    pass

# For updating client (all fields optional)
class ClientUpdate(BaseModel):
    name: constr(min_length=3, max_length=50) | None = None
    email: EmailStr | None = None
    client_type: ClientTypeEnum | None = None
    phone: constr(min_length=10, max_length=15) | None = None

    @validator("phone")
    def validate_phone(cls, value):
        if value:
            pattern = re.compile(r"^[0-9]{10,15}$")
            if not pattern.match(value):
                raise ValueError("Phone must contain only digits (10-15 characters)")
        return value

# Response schema
class ClientResponse(ClientBase):
    id: int

    class Config:
        orm_mode = True  # Convert SQLAlchemy → JSON
