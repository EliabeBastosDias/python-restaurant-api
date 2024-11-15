from internal.core.domain.menu import Menu
from internal.core.domain.user import User
from internal.repositories.menurepo import MenuRepository
from internal.repositories.userrepo import UserRepository


class Repositories():
    def __init__(self, connections):
        self.__connections = connections
        self.menu = MenuRepository(self.__connections.core_database_session, Menu)
        self.user = UserRepository(self.__connections.core_database_session, User)
    
