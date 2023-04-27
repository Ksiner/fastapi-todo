import os
from dotenv import load_dotenv

load_dotenv()

assert os.getenv("SQLALCHEMY_DB_URL") is not None
assert os.getenv("JWT_SECRET_KEY") is not None


class Configs:
    SQLALCHEMY_DB_URL: str = os.getenv("SQLALCHEMY_DB_URL")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM") or "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = (
        int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")) if os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES") else 30
    )
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES = (
        int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_MINUTES")) if os.getenv("JWT_REFRESH_TOKEN_EXPIRE_MINUTES") else 10080
    )
