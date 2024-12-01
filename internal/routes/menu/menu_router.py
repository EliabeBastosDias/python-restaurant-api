from fastapi import APIRouter
from pydantic import BaseModel

from internal.controllers.menu.menu_controller import MenuController
from internal.controllers.menu.menu_swagger import (
    CreateMenuResponseModel,
    ListMenuResponseModel,
    MenuNullResponseModel,
    MenuResponseModel,
)
from internal.errors.error_swagger import ErrorResponseModel


class MenuRouter:
    def __init__(self, menucontroller: MenuController):
        self.router = APIRouter(prefix="/menus")
        self.__menucontroller = menucontroller
        self.__default_responses = {
            404: {"model": ErrorResponseModel},
            422: {"model": ErrorResponseModel},
            500: {"model": ErrorResponseModel},
        }
        self.router.add_api_route(
            path="/",
            endpoint=self.__menucontroller.create_action,
            methods=["POST"],
            status_code=201,
            responses=self.__add_responses(
                CreateMenuResponseModel, self.__default_responses
            ),
        )
        self.router.add_api_route(
            path="/{menu_token}",
            endpoint=self.__menucontroller.get_action,
            methods=["GET"],
            status_code=200,
            responses=self.__add_responses(MenuResponseModel, self.__default_responses),
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.__menucontroller.list_action,
            methods=["GET"],
            status_code=200,
            responses=self.__add_responses(
                ListMenuResponseModel, self.__default_responses
            ),
        )
        self.router.add_api_route(
            path="/{menu_token}",
            endpoint=self.__menucontroller.update_action,
            methods=["PUT"],
            status_code=200,
            responses=self.__add_responses(MenuResponseModel, self.__default_responses),
        )
        self.router.add_api_route(
            path="/{menu_token}/inactivate",
            endpoint=self.__menucontroller.inactivate_action,
            methods=["PATCH"],
            status_code=200,
            responses=self.__add_responses(
                MenuNullResponseModel, self.__default_responses
            ),
        )

    def __add_responses(
        self, success_model: BaseModel, default_responses: dict
    ) -> dict:
        return {200: {"model": success_model}, **default_responses}
