from fastapi import FastAPI
from sqlalchemy.orm.session import Session
from internal.controllers.controllers import Controllers
from internal.database.core_connection import DatabaseCoreConnection
from internal.repositories.repositories import Repositories
from internal.routes.router import Router




class HttpServer:
    def __init__(self) -> None:
        self.__app = FastAPI()

    def setup(self):
        repositories = Repositories()
        controllers = Controllers(repositories)
        Router(self.__app, controllers).setup()
    def get_app(self):
        return self.__app
