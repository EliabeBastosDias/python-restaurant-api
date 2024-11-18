import os
from enum import Enum
from dotenv import load_dotenv


class EnvKey(Enum):
    SERVER_PORT = "SERVER_PORT"
    DB_DRIVER = "DB_DRIVER"
    DB_TYPE = "DB_TYPE"
    DB_USER = "DB_USER"
    DB_PASSWORD = "DB_PASSWORD"
    DB_HOST = "DB_HOST"
    DB_PORT = "DB_PORT"
    DB_NAME = "DB_NAME"
    DB_OPTIONS = "DB_OPTIONS"
    JWT_SECRET = "JWT_SECRET"


class EnvHandler:
    def get(key: EnvKey) -> str:
        return os.getenv(key.value, "")

    def get_int(key: EnvKey) -> int:
        value = os.getenv(key.value, "0")
        try:
            return int(value)
        except ValueError:
            return 0

    def load():
        load_dotenv()
