from internal.common.response_formatter import ResponseFormatter
from internal.controllers.menu.menu_controller import MenuController
from internal.controllers.user.user_controller import UserController
from internal.errors.error_handler import ErrorHandler
from internal.repositories.repositories import Repositories


class Controllers:
    def __init__(
        self,
        repositories: Repositories,
        error_handler: ErrorHandler,
        formatter: ResponseFormatter,
    ) -> None:
        self.menu = MenuController(repositories.menu, error_handler, formatter)
        self.user = UserController(repositories.user)
