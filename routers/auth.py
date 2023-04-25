from fastapi import APIRouter
from dto import auth as AuthDTO
from services.auth import AuthService

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/register")
async def register(dto: AuthDTO.RegistrationRequestDTO) -> AuthDTO.AuthResponseDTO:
    token_result = await AuthService.basic_register(
        email=dto.email, password=dto.password, first_name=dto.first_name, last_name=dto.last_name
    )

    return AuthDTO.AuthResponseDTO(**token_result)


@router.post("authorize")
async def authorize(dto: AuthDTO.AuthRequestDTO) -> AuthDTO.AuthResponseDTO:
    token_result = await AuthService.basic_authorize(email=dto.email, password=dto.password)

    return AuthDTO.AuthResponseDTO(**token_result)


@router.post("refresh-token")
async def refresh_token(dto: AuthDTO.RefreshTokenRequestDTO) -> AuthDTO.AuthResponseDTO:
    token_result = await AuthService.basic_authorize(email=dto.email, password=dto.password)

    return AuthDTO.AuthResponseDTO(**token_result)
