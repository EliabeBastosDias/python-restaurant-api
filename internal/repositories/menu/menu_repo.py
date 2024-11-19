from internal.database.core_connection import DatabaseCoreConnection
from internal.repositories.base_repo import BaseRepository
from internal.core.domain.menu import Menu


class MenuRepository(BaseRepository[Menu]):
    def getByName(self, name: str):
        with DatabaseCoreConnection() as session:
            return session.query(self._model).filter_by(name=name).first()
