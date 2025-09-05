# Import Pydantic base model and EmailStr type
from pydantic import BaseModel, EmailStr


# Base schema that defines common fields for a User
class UserBase(BaseModel):
    name: str
    email: EmailStr


# Schema for creating a new user → same as UserBase
class UserCreate(UserBase):
    # 'pass' means we don't add new fields, it inherits everything from UserBase
    pass


# Schema for updating an existing user → also same as UserBase
class UserUpdate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True


class Query_Out(UserBase):
    name: str
    email: str
    search: str
    class Config:
        orm_mode = True
