from fastapi import FastAPI
from internal.controllers.controllers import Controllers
from internal.database.core_connection import DatabaseCoreConnection
from internal.repositories.repositories import Repositories
from internal.routes.router import Router


class Connections:
    def __init__(self, core_database) -> None:
        self.core_database_session = core_database


class HttpServer:
    def __init__(self) -> None:
        self.__app = FastAPI()

    def setup(self):
        connections = self.setup_connections()
        repositories = Repositories(connections)
        controllers = Controllers(repositories)
        Router(self.__app, controllers).setup()

    def setup_connections(self):
        session = DatabaseCoreConnection().get_session()
        connections = Connections(session)
        return connections

    def get_app(self):
        return self.__app
