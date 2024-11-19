from datetime import datetime
from fastapi.responses import JSONResponse

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
    MenuResponseDTO,
)


class MenuController:
    def __init__(self, menurepo: MenuRepository) -> None:
        self.__menurepo = menurepo

    def create_action(self, body: MenuRequestDTO):
        result = CreateMenuCommand(self.__menurepo).execute(body)
        
        response_dict = result.__dict__.copy()

        for key, value in response_dict.items():
            if isinstance(value, datetime):
                response_dict[key] = value.isoformat()


        return JSONResponse(status_code=201, content=response_dict)

    def get_action(self, menu_token):
        execute_params = GetMenuRequestDTO(token=menu_token)
        result = GetMenuCommand(self.__menurepo).execute(execute_params)
        return JSONResponse(status_code=200, content=result)

    def list_action(self, active: bool = False, page: int = 1):
        execute_params = ListMenuRequestDTO(onlyActives=active, page=page)
        result = ListMenuCommand(self.__menurepo).execute(execute_params)
        return JSONResponse(status_code=200, content=result)

    def update_action(self, body: MenuRequestDTO, menu_token: str = None):
        result = UpdateMenuCommand(self.__menurepo).execute(body, menu_token)
        return JSONResponse(status_code=200, content=result)

    def inactivate_action(self, menu_token: str = None):
        execute_params = InactivateMenuRequestDTO(token=menu_token)
        result = InactivateMenuCommand(self.__menurepo).execute(execute_params)
        return JSONResponse(status_code=200, content=result)
