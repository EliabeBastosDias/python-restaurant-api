from internal.core.domain.menu import Menu
from internal.core.domain.user import User
from internal.repositories.menu_repo import MenuRepository
from internal.repositories.user_repo import UserRepository


class Repositories:
    def __init__(self, connections):
        self.__connections = connections
        self.menu = MenuRepository(self.__connections, Menu)
        self.user = UserRepository(self.__connections, User)
