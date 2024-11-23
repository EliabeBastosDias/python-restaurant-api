from typing import TypeVar, List
from internal.common.response_schema import ResponseModel
from internal.controllers.menu.menu_schema import MenuResponseDTO

T = TypeVar("T")


class MenuResponseModel(ResponseModel[MenuResponseDTO]):
    pass


class ListMenuResponseModel(ResponseModel[List[MenuResponseDTO]]):
    pass
