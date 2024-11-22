from internal.common.response_formatter import ResponseFormatter
from internal.controllers.menu.menu_controller import MenuController
from internal.controllers.user.user_controller import UserController
from internal.repositories.repositories import Repositories


class Controllers:
    def __init__(self, repositories: Repositories, formatter: ResponseFormatter) -> None:
        self.menu = MenuController(repositories.menu, formatter)
        self.user = UserController(repositories.user)
