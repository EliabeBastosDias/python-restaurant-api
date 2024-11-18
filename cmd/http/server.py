from fastapi import FastAPI
from sqlalchemy.orm.session import Session
from internal.controllers.controllers import Controllers
from internal.database.core_connection import DatabaseCoreConnection
from internal.repositories.repositories import Repositories
from internal.routes.router import Router

from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Menu(Base):
    __tablename__ = "menus"

    token = Column(String, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    active = Column(Boolean, default=True)


class Connections:
    def __init__(self, core_database: Session) -> None:
        self.core_database_session = core_database


class HttpServer:
    def __init__(self) -> None:
        self.__app = FastAPI()

    def setup(self):
        connections = self.setup_connections()
        repositories = Repositories(connections.core_database_session)
        controllers = Controllers(repositories)
        Router(self.__app, controllers).setup()

    def setup_connections(self):
        session = DatabaseCoreConnection().get_session()
        connections = Connections(session)
        return connections

    def get_app(self):
        return self.__app
