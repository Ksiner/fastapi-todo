import os
from dotenv import load_dotenv

load_dotenv()


class Configs:
    SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DB_URL")
