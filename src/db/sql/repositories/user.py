from sqlalchemy.orm import Session
from typing import Union
from db.exceptions import NotFoundException
import models


class UserRepository:
    _model = models.User

    def get_by_id(self, db: Session, email: str):
        return db.query(self._model).filter(self._model.email == email).first()

    def create(
        self, db: Session, email: str, hashed_password: str, first_name: Union[str, None], last_name: Union[str, None]
    ):
        db_user = self._model(email=email, password=hashed_password, first_name=first_name, last_name=last_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    def update(
        self,
        db: Session,
        id: str,
        email: Union[str, None],
        hashed_password: Union[str, None],
        first_name: Union[str, None],
        last_name: Union[str, None],
    ):
        db_user = db.get(self._model, id)

        if not db_user:
            raise NotFoundException(message="User not found")

        if email:
            db_user.email = email

        if hashed_password:
            db_user.password = hashed_password

        if first_name:
            db_user.first_name = first_name

        if last_name:
            db_user.last_name = last_name

        db.commit()
        db.refresh(db_user)

        return db_user


UserRepositoryInstance = UserRepository()
