from fastapi.responses import PlainTextResponse

from internal.routes.menurouter import MenuRouter
from internal.routes.userrouter import UserRouter


class Router:
    def __init__(self, app, controllers):
        self.__app = app
        self.__controllers = controllers

    def setup(self):
        @self.__app.get("/")
        def hello():
            return  {"message": "system running"}
        
        MenuRouter(self.__app, self.__controllers.menu).setup()
        UserRouter(self.__app, self.__controllers.user).setup()