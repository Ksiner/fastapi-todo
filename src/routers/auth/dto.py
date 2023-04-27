from typing import Union
from pydantic import BaseModel, EmailStr, Field


class CredentialsDTO(BaseModel):
    email: EmailStr = Field(example="text@gmail.com")
    password: str


class AuthRequestDTO(CredentialsDTO):
    pass


class RegistrationRequestDTO(CredentialsDTO):
    first_name: Union[str, None]
    last_name: Union[str, None]

    class Config:
        orm_mode = True


class RefreshTokenRequestDTO(BaseModel):
    refresh_token: str


class TokenDTO(BaseModel):
    token: str
    expires_at: int


class AuthResponseDTO(BaseModel):
    access_token: TokenDTO
    refresh_token: TokenDTO
