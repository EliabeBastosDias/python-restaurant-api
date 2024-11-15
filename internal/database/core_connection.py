import os

from internal.envs import EnvHandler, EnvKey

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

CORE_DSN = "{}+{}://{}:{}@{}:{}/{}?{}".format(
    EnvHandler.get(EnvKey.DB_TYPE),
    EnvHandler.get(EnvKey.DB_DRIVER),
    EnvHandler.get(EnvKey.DB_USER),
    EnvHandler.get(EnvKey.DB_PASSWORD),
    EnvHandler.get(EnvKey.DB_HOST),
    EnvHandler.get_int(EnvKey.DB_PORT),
    EnvHandler.get(EnvKey.DB_NAME),
    EnvHandler.get(EnvKey.DB_OPTIONS),
)

class DatabaseCoreConnection:
    def __init__(self) -> None:
        engine = create_engine(CORE_DSN)
        event.listen(engine, "connect", self.__set_search_path)
        self.__engine = engine

    def get_session(self):
        session_maker = sessionmaker(bind=self.__engine)
        return session_maker()

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def __set_search_path(self, dbapi_connection, connection_record):
        with dbapi_connection.cursor() as cursor:
            cursor.execute("SET search_path TO app")
