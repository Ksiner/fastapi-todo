import sqlalchemy as sa
from db.sql.core import TableNames
from uuid import uuid4
from datetime import datetime

from db.sql.core import Base


class User(Base):
    __tablename__ = TableNames.USERS.value

    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)

    email = sa.Column(sa.Text)
    password = sa.Column(sa.Text)

    created_at = sa.Column(sa.DateTime, default=datetime.now)
