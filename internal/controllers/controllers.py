from internal.controllers.menu.menucontroller import MenuController
from internal.controllers.user.usercontroller import UserController
from internal.repositories.repositories import Repositories


class Controllers:
    def __init__(self, repositories: Repositories) -> None:
        self.menu = MenuController(repositories.menu)
        self.user = UserController(repositories.user)
