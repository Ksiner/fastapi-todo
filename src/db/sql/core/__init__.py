from .core import Base, SessionLocal
from enum import Enum


class TableNames(Enum):
    USERS = "users"
