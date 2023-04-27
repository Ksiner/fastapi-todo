from .types import TokenResult, TokenCreationResult
from config import Configs
from datetime import datetime, timedelta
from jose import jwt


class IssueTokenFeature:
    def _create_jwt(self, payload: dict, expires_in_minutes: int | None = None) -> TokenCreationResult:
        to_encode = payload.copy()

        if expires_in_minutes:
            expires_at = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
        else:
            expires_at = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expires_at})

        encoded_jwt = jwt.encode(claims=to_encode, key=Configs.JWT_SECRET_KEY, algorithm=Configs.JWT_ALGORITHM)

        return {"token": encoded_jwt, "expires_at": int(expires_at.timestamp() * 1000)}

    def execute(self, user_id: str) -> TokenResult:
        access_token = self._create_jwt(
            payload={"user_id": user_id, "aud": "access"},
            expires_in_minutes=Configs.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
        )

        refresh_token = self._create_jwt(
            payload={"user_id": user_id, "aud": "refresh"},
            expires_in_minutes=Configs.JWT_REFRESH_TOKEN_EXPIRE_MINUTES,
        )

        return {"access_token": access_token, "refresh_token": refresh_token}


IssueTokenFeatureInstance = IssueTokenFeature()
