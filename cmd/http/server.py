from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from internal.common.response_formatter import ResponseFormatter
from internal.controllers.controllers import Controllers
from internal.errors.error_handler import ErrorHandler
from internal.repositories.repositories import Repositories
from internal.routes.router import Router


class HttpServer:
    def __init__(self) -> None:
        self.__app = FastAPI()

    def setup(self):
        formatter = self.utilities()
        error_handler = self.setup_error_handler(formatter)
        repositories = Repositories()
        controllers = Controllers(repositories, error_handler, formatter)
        Router(self.__app, controllers).setup()

    def utilities(self) -> ResponseFormatter:
        formatter = ResponseFormatter()
        return formatter

    def setup_error_handler(self, formatter: ResponseFormatter) -> ErrorHandler:
        error_handler = ErrorHandler(formatter)
        self.__app.add_exception_handler(
            RequestValidationError, error_handler.handle_validation_errors
        )
        return error_handler

    def get_app(self):
        return self.__app
