from fastapi import APIRouter


from internal.controllers.menu.menucontroller import MenuController


class MenuRouter:
    def __init__(self, menucontroller: MenuController):
        self.router = APIRouter(prefix="/menus")
        self.__menucontroller = menucontroller
        self.router.add_api_route(
            path="/", endpoint=self.__menucontroller.create_action, methods=["POST"]
        )
        self.router.add_api_route(
            path="/{menu_token}",
            endpoint=self.__menucontroller.get_action,
            methods=["GET"],
        )
        self.router.add_api_route(
            path="/", endpoint=self.__menucontroller.list_action, methods=["GET"]
        )
        self.router.add_api_route(
            path="/{menu_token}",
            endpoint=self.__menucontroller.update_action,
            methods=["PUT"],
        )
        self.router.add_api_route(
            path="/{menu_token}/inactivate",
            endpoint=self.__menucontroller.inactivate_action,
            methods=["PATCH"],
        )
