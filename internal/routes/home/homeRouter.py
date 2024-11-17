from fastapi import APIRouter


class HomeRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(path="/", endpoint=self.hello, methods=["GET"])

    def hello(self):
        return {"message": "system running"}
