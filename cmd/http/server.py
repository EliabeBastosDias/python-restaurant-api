from fastapi import FastAPI
from h11 import Response
from sqlalchemy.orm.session import Session
from internal.common.response_formatter import ResponseFormatter
from internal.controllers.controllers import Controllers
from internal.database.core_connection import DatabaseCoreConnection
from internal.repositories.repositories import Repositories
from internal.routes.router import Router




class HttpServer:
    def __init__(self) -> None:
        self.__app = FastAPI()

    def setup(self):
        formatter = self.utilities()
        repositories = Repositories()
        controllers = Controllers(repositories, formatter)
        Router(self.__app, controllers).setup()
    
    def utilities(self) -> ResponseFormatter:
        formatter = ResponseFormatter()
        return formatter
    def get_app(self):
        return self.__app
