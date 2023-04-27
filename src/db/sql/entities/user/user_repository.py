from sqlalchemy.orm import Session
from db.exceptions import NotFoundException
from .user_model import User as UserModel
from .types import UserCreatePayload, UserUpdatePayload


class UserRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def get_by_id(self, email: str):
        return self._db.query(UserModel).filter(UserModel.email == email).first()

    def create(self, payload: UserCreatePayload):
        db_user = UserModel(
            email=payload.get("email"),
            password=payload.get("hashed_password"),
            first_name=payload.get("last_name"),
            last_name=payload.get("last_name"),
        )

        self._db.add(db_user)
        self._db.flush()
        self._db.refresh(db_user)

        return db_user

    def update(self, payload: UserUpdatePayload):
        db_user = self._db.get(UserModel, id)

        if not db_user:
            raise NotFoundException(message="User not found")

        if payload.get("email"):
            db_user.email = payload["email"]

        if payload.get("hashed_password"):
            db_user.password = payload["hashed_password"]

        if payload.get("first_name"):
            db_user.first_name = payload["first_name"]

        if payload.get("last_name"):
            db_user.last_name = payload["last_name"]

        return db_user
