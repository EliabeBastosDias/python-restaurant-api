from fastapi import FastAPI

from internal.controllers.controllers import Controllers
from internal.routes.home.homeRouter import HomeRouter
from internal.routes.menu.menu_router import MenuRouter


class Router:
    def __init__(self, app: FastAPI, controllers: Controllers):
        self.__app = app
        self.__controllers = controllers

    def setup(self):
        self.__app.include_router(HomeRouter().router)
        self.__app.include_router(MenuRouter(self.__controllers.menu).router)
        # self.__app.include_router(UserRouter(self.__controllers.user).router)
