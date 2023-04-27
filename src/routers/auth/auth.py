from fastapi import APIRouter, Depends
from .dto import AuthRequestDTO, AuthResponseDTO, RefreshTokenRequestDTO, RegistrationRequestDTO
from features.auth.register_basic_feature import RegisterBasicFeature
from features.auth.authorize_basic_feature import AuthorizeBasicFeature
from features.auth.refresh_token_feature import RefreshTokenFeature
from routers.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/register")
async def register(dto: RegistrationRequestDTO, db: Session = Depends(get_db)) -> AuthResponseDTO:
    token_result = await RegisterBasicFeature(db=db).execute(payload=dto)

    return AuthResponseDTO(**token_result)


@router.post("authorize")
async def authorize(dto: AuthRequestDTO, db: Session = Depends(get_db)) -> AuthResponseDTO:
    token_result = await AuthorizeBasicFeature(db=db).execute(email=dto.email, password=dto.password)

    return AuthResponseDTO(**token_result)


@router.post("refresh-token")
async def refresh_token(dto: RefreshTokenRequestDTO, db: Session = Depends(get_db)) -> AuthResponseDTO:
    token_result = await RefreshTokenFeature(db=db).execute(email=dto.email, password=dto.password)

    return AuthResponseDTO(**token_result)
