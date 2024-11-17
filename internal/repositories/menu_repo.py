from internal.repositories.base_repo import BaseRepository
from internal.core.domain.menu import Menu


class MenuRepository(BaseRepository[Menu]):
    def getByName(self, name: str):
        return self.__session.query(self.__model).filter_by(name=name).first()
