from pydantic import BaseModel
from .user import UserCreateDTO, UserBaseDTO


class RegistrationRequestDTO(UserCreateDTO):
    pass


class AuthRequestDTO(UserBaseDTO):
    pass


class RefreshTokenRequestDTO(BaseModel):
    refresh_token: str


class AuthResponseDTO(BaseModel):
    access_token: str
    expires_at: int
    refresh_token: str
