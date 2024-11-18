from internal.envs import EnvHandler, EnvKey

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CORE_DSN = "{}+{}://{}:{}@{}:{}/{}".format(
    EnvHandler.get(EnvKey.DB_TYPE),
    EnvHandler.get(EnvKey.DB_DRIVER),
    EnvHandler.get(EnvKey.DB_USER),
    EnvHandler.get(EnvKey.DB_PASSWORD),
    EnvHandler.get(EnvKey.DB_HOST),
    EnvHandler.get_int(EnvKey.DB_PORT),
    EnvHandler.get(EnvKey.DB_NAME),
)


class DatabaseCoreConnection:
    def __init__(self) -> None:
        self.__engine = create_engine(CORE_DSN)
        self.__session_maker = sessionmaker(bind=self.__engine)
        # event.listen(self.__engine, "connect", self.__set_search_path)

    def get_session(self):
        return self.__session_maker()

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    # def __set_search_path(self, dbapi_connection, connection_record):
    #     with dbapi_connection.cursor() as cursor:
    #         cursor.execute("SET search_path TO app")
