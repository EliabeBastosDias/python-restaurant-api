from pyexpat import model
from internal.core.domain.menu import Menu
from internal.core.domain.user import User
from internal.repositories.menu.menu_repo import MenuRepository
from internal.repositories.user.user_repo import UserRepository


class Repositories:
    def __init__(self):
        self.menu = MenuRepository(model=Menu)
        self.user = UserRepository(model=User)
