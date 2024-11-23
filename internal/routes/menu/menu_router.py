from fastapi import APIRouter

from internal.controllers.menu.menu_controller import MenuController
from internal.controllers.menu.menu_swagger import MenuResponseModel


class MenuRouter:
    def __init__(self, menucontroller: MenuController):
        self.router = APIRouter(prefix="/menus")
        self.__menucontroller = menucontroller
        self.router.add_api_route(
            path="/",
            endpoint=self.__menucontroller.create_action,
            methods=["POST"],
            status_code=201,
            response_model=MenuResponseModel,
        )
        self.router.add_api_route(
            path="/{menu_token}",
            endpoint=self.__menucontroller.get_action,
            methods=["GET"],
            status_code=200,
            response_model=MenuResponseModel,
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.__menucontroller.list_action,
            methods=["GET"],
            status_code=200,
        )
        self.router.add_api_route(
            path="/{menu_token}",
            endpoint=self.__menucontroller.update_action,
            methods=["PUT"],
            status_code=200,
        )
        self.router.add_api_route(
            path="/{menu_token}/inactivate",
            endpoint=self.__menucontroller.inactivate_action,
            methods=["PATCH"],
            status_code=200,
        )
