from typing import Union
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, UUID4


class UserBaseDTO(BaseModel):
    email: EmailStr = Field(example="text@gmail.com")
    password: str


class UserCreateDTO(UserBaseDTO):
    first_name: Union[str, None]
    last_name: Union[str, None]


class UserUpdateDTO(BaseModel):
    email: Union[EmailStr, None] = Field(example="text@gmail.com")
    password: Union[str, None]
    first_name: Union[str, None]
    last_name: Union[str, None]


class UserDTO(BaseModel):
    id: UUID4
    email: EmailStr = Field(example="text@gmail.com")
    first_name: Union[str, None]
    last_name: Union[str, None]
    created_at: datetime

    class Config:
        orm_mode = True
