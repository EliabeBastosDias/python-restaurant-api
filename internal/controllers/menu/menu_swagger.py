from typing import TypeVar
from internal.common.response_schema import ResponseModel
from internal.controllers.menu.menu_schema import MenuResponseDTO

T = TypeVar("T")


class MenuResponseModel(ResponseModel[MenuResponseDTO]):
    pass







