from internal.core.usecases.create_menu_command.create_menu_cmd import CreateMenuCommand
from internal.core.usecases.get_menu_command.get_menu_cmd import GetMenuCommand
from internal.core.usecases.inactivate_menu_command.inactivate_menu_cmd import InactivateMenuCommand
from internal.core.usecases.list_menu_command.list_menu_cmd import ListMenuCommand
from internal.core.usecases.update_menu_command.update_menu_cmd import UpdateMenuCommand
from internal.routes.menurouter import MenuUpdateRequest
from pkg.json.main import JsonHandler


class MenuController:
    def __init__(self, menurepo) -> None:
        self.__menurepo = menurepo
    
    def create_action(self, body):
        execute_params = body
        result = CreateMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)

    def get_action(self, menu_token):
        execute_params = {"token": menu_token}
        result = GetMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)
    
    def list_action(self, menu_token: str = None, active: bool = False, page: int = 1):
        execute_params = {"token": menu_token, "active": active, "page": page}
        result = ListMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)

    def update_action(self, body: MenuUpdateRequest, menu_token: str = None):
        execute_params = {"token": menu_token, "name": body.name}
        result = UpdateMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)

    def inactivate_action(self, menu_token: str = None):
        execute_params = {"token": menu_token}
        result = InactivateMenuCommand(self.__menurepo).execute(execute_params)
        return JsonHandler.serialize_result(result)