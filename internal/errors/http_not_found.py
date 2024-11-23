from fastapi.exceptions import HTTPException


class HttpNotFoundError(HTTPException):
    def __init__(self, message: str) -> None:
        super().__init__(
            status_code=404, detail={"message": message, "title": "Not Found"}
        )
