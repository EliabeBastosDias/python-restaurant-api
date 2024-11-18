from fastapi.responses import JSONResponse
from internal.controllers.menu.menu_params import (
    CreateMenuParams,
    GetParams,
    InactivateMenuParams,
    ListMenuParams,
    UpdateMenuParams,
)
from internal.core.usecases.menu import (
    CreateMenuCommand,
    GetMenuCommand,
    ListMenuCommand,
    UpdateMenuCommand,
    InactivateMenuCommand,
)
from internal.repositories.menu_repo import MenuRepository
from internal.controllers.menu.menu_schema import MenuCreateSchema, MenuUpdateSchema
from pkg.json.main import JsonHandler


class MenuController:
    def __init__(self, menurepo: MenuRepository) -> None:
        self.__menurepo = menurepo

    def create_action(self, body: MenuCreateSchema):
        execute_params = CreateMenuParams(**body.model_dump())
        CreateMenuCommand(self.__menurepo).execute(execute_params)

        return JSONResponse(status_code=201, content="oi")

    def get_action(self, menu_token):
        execute_params = GetParams(token=menu_token)
        result = GetMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)

    def list_action(self, active: bool = False, page: int = 1):
        execute_params = ListMenuParams(onlyActives=active, page=page)
        result = ListMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)

    def update_action(self, body: MenuUpdateSchema, menu_token: str = None):
        execute_params = UpdateMenuParams(**body.model_dump())
        result = UpdateMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)

    def inactivate_action(self, menu_token: str = None):
        execute_params = InactivateMenuParams(token=menu_token)
        result = InactivateMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)
