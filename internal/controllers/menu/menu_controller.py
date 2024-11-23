from internal.common.response_formatter import ResponseFormatter
from internal.common.response_schema import ResponseModel
from internal.core.usecases.menu import (
    CreateMenuCommand,
    GetMenuCommand,
    ListMenuCommand,
    UpdateMenuCommand,
    InactivateMenuCommand,
)
from internal.repositories.menu.menu_repo import MenuRepository
from internal.controllers.menu.menu_schema import (
    GetMenuRequestDTO,
    InactivateMenuRequestDTO,
    ListMenuRequestDTO,
    MenuRequestDTO,
)


class MenuController:
    def __init__(self, menurepo: MenuRepository, formatter: ResponseFormatter) -> None:
        self.__menurepo = menurepo
        self.__formatter = formatter

    def create_action(self, body: MenuRequestDTO) -> ResponseModel:
        result = CreateMenuCommand(self.__menurepo).execute(body)
        response = self.__formatter.format_response(
            status_code=201, message="Menu created", data=result
        )
        return response

    def get_action(self, menu_token) -> ResponseModel:
        execute_params = GetMenuRequestDTO(token=menu_token)
        result = GetMenuCommand(self.__menurepo).execute(execute_params)
        response = self.__formatter.format_response(
            status_code=200, message="Menu retrieved", data=result
        )
        return response

    def list_action(self, active: bool = False, page: int = 1) -> ResponseModel:
        execute_params = ListMenuRequestDTO(onlyActives=active, page=page)
        result = ListMenuCommand(self.__menurepo).execute(execute_params)
        response = self.__formatter.format_response(
            status_code=200, message="Menus retrieved", data=result
        )
        return response

    def update_action(
        self, body: MenuRequestDTO, menu_token: str = None
    ) -> ResponseModel:
        result = UpdateMenuCommand(self.__menurepo).execute(body, menu_token)
        response = self.__formatter.format_response(
            status_code=200, message="Menu updated", data=result
        )
        return response

    def inactivate_action(self, menu_token: str = None) -> ResponseModel:
        execute_params = InactivateMenuRequestDTO(token=menu_token)
        InactivateMenuCommand(self.__menurepo).execute(execute_params)
        response = self.__formatter.format_response(
            status_code=200, message="Menu deleted"
        )
        return response
