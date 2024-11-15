from internal.controllers.menucontroller import MenuController
from internal.controllers.usercontroller import UserController


class Controllers:
    def __init__(self, repositories) -> None:
        self.menu = MenuController(repositories.menu)
        self.user = UserController(repositories.user)