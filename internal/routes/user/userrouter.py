from fastapi import APIRouter

from internal.controllers.user.usercontroller import UserController


class UserRouter:
    def __init__(self, usercontroller: UserController):
        self.router = APIRouter(prefix="/users")
        self.__usercontroller = usercontroller
        self.router.add_api_route(
            path="/", endpoint=self.__usercontroller.create, methods=["POST"]
        )
        self.router.add_api_route(
            path="/{user_token}", endpoint=self.__usercontroller.get, methods=["GET"]
        )
