from fastapi import Request, Response
from internal.common.response_formatter import ResponseFormatter
from internal.common.response_schema import ResponseModel
from internal.core.usecases.menu import (
    CreateMenuCommand,
    GetMenuCommand,
    ListMenuCommand,
    UpdateMenuCommand,
    InactivateMenuCommand,
)
from internal.errors.error_handler import ErrorHandler
from internal.repositories.menu.menu_repo import MenuRepository
from internal.controllers.menu.menu_schema import (
    GetMenuRequestDTO,
    InactivateMenuRequestDTO,
    ListMenuRequestDTO,
    MenuRequestDTO,
)


class MenuController:
    def __init__(
        self,
        menurepo: MenuRepository,
        error_handler: ErrorHandler,
        formatter: ResponseFormatter,
    ) -> None:
        self.__menurepo = menurepo
        self.__formatter = formatter
        self.__error_handler = error_handler

    def create_action(
        self, request: Request, response: Response, body: MenuRequestDTO
    ) -> ResponseModel:
        try:
            result = CreateMenuCommand(self.__menurepo).execute(body)
            formatted_result = self.__formatter.format_response(
                status_code=201, message="Menu created", data=result
            )
        except Exception as e:
            formatted_result = self.__error_handler.handle_errors(request, e)
            response.status_code = formatted_result.status_code
        return formatted_result

    def get_action(
        self, request: Request, response: Response, menu_token
    ) -> ResponseModel:
        try:
            execute_params = GetMenuRequestDTO(token=menu_token)
            result = GetMenuCommand(self.__menurepo).execute(execute_params)
            formatted_result = self.__formatter.format_response(
                status_code=200, message="Menu retrieved", data=result
            )
        except Exception as e:
            formatted_result = self.__error_handler.handle_errors(request, e)
            response.status_code = formatted_result.status_code
        return formatted_result

    def list_action(
        self, request: Request, response: Response, active: bool = False, page: int = 1
    ) -> ResponseModel:
        try:
            execute_params = ListMenuRequestDTO(onlyActives=active, page=page)
            result = ListMenuCommand(self.__menurepo).execute(execute_params)
            formatted_result = self.__formatter.format_response(
                status_code=200, message="Menus retrieved", data=result
            )
        except Exception as e:
            formatted_result = self.__error_handler.handle_errors(request, e)
            response.status_code = formatted_result.status_code
        return formatted_result

    def update_action(
        self,
        request: Request,
        response: Response,
        body: MenuRequestDTO,
        menu_token: str = None,
    ) -> ResponseModel:
        try:
            result = UpdateMenuCommand(self.__menurepo).execute(body, menu_token)
            formatted_result = self.__formatter.format_response(
                status_code=200, message="Menu updated", data=result
            )
        except Exception as e:
            formatted_result = self.__error_handler.handle_errors(request, e)
            response.status_code = formatted_result.status_code
        return formatted_result

    def inactivate_action(
        self, request: Request, response: Response, menu_token: str = None
    ) -> ResponseModel:
        try:
            execute_params = InactivateMenuRequestDTO(token=menu_token)
            InactivateMenuCommand(self.__menurepo).execute(execute_params)
            formatted_result = self.__formatter.format_response(
                status_code=200, message="Menu deleted"
            )
        except Exception as e:
            formatted_result = self.__error_handler.handle_errors(request, e)
            response.status_code = formatted_result.status_code
        return formatted_result
