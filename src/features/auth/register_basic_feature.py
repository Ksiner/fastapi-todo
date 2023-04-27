from .types import TokenResult
from typing import Union, TypedDict
from utils.mixins import DBSessionMixin
from sqlalchemy.orm import Session
from .issue_token_feature import IssueTokenFeatureInstance
from db.sql.entities.user.user_repository import UserRepository
from utils.hashing import hash_content


class RegisterUserPayload:
    email: str
    password: str
    first_name: Union[str, None]
    last_name: Union[str, None]


class RegisterBasicFeature(DBSessionMixin):
    def __init__(self, db: Session):
        super().__init__(db=db)

        self._user_repository = UserRepository(db=db)

    async def execute(self, payload: RegisterUserPayload) -> TokenResult:
        with self._db.begin():
            new_user = self._user_repository.create(
                payload={
                    "email": payload.email,
                    "hashed_password": hash_content(payload.password),
                    "first_name": payload.first_name,
                    "last_name": payload.last_name,
                }
            )

            return IssueTokenFeatureInstance.execute(user_id=str(new_user.id))
