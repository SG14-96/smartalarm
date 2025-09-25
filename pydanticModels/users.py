from pydantic import BaseModel
from typing import Optional

class PydanticUser(BaseModel):
    id: int
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    roles: Optional[list] = []

class PydanticUserInDB(PydanticUser):
    hashed_password: str

class PydanticUserCreate(PydanticUser):
    email: str
    full_name: str
    password: str