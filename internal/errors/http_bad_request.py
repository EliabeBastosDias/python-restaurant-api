from fastapi.exceptions import HTTPException


class HttpBadRequestError(HTTPException):
    def __init__(self, message: str) -> None:
        super().__init__(
            status_code=400, detail={"message": message, "title": "Bad Request"}
        )
