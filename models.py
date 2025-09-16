from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    email: str
    full_name: str
    password: str