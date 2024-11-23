from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from internal.common.response_formatter import ResponseFormatter
from internal.common.response_schema import ResponseModel


class ErrorHandler:
    def __init__(self, formatter: ResponseFormatter) -> None:
        self.__formatter = formatter

    def handle_validation_errors(
        self, request: Request, exc: RequestValidationError
    ) -> BaseModel:
        errors_dictionary = self.__filter_request_validator_errors(exc)
        response = self.__formatter.format_response(
            422, "Unprocessable Entity", errors_dictionary, True
        )
        return JSONResponse(
            status_code=response.status_code, content=response.model_dump()
        )

    def handle_errors(self, request: Request, exc: Exception) -> ResponseModel:
        if isinstance(exc, HTTPException):
            if isinstance(exc.detail, dict):
                title = exc.detail.get("title", "Error")
                message = exc.detail.get("message", "An error occurred")
            else:
                title = "Error"
                message = exc.detail if exc.detail else "An error occurred"
            response = self.__formatter.format_response(
                exc.status_code, title, message, True
            )
        else:
            response = self.__formatter.format_response(
                500, "Internal Server Error", str(exc), True
            )
        return response

    def __filter_request_validator_errors(self, exc: RequestValidationError) -> dict:
        errors = exc.errors()
        filtered_errors = []
        for error in errors:
            filtered_error = {
                "msg": error["msg"],
                "input": error.get("input", "N/A"),
                "location": error["loc"][1] if len(error["loc"]) > 1 else "N/A",
            }
            filtered_errors.append(filtered_error)
        errors_dictionary = {"errors": filtered_errors}
        return errors_dictionary
