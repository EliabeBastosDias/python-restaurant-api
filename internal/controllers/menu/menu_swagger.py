from typing import TypeVar, List
from internal.common.response_schema import ResponseModel
from internal.controllers.menu.menu_schema import CreateMenuResponseDTO, MenuResponseDTO

T = TypeVar("T")


class MenuResponseModel(ResponseModel[MenuResponseDTO]):
    pass


class CreateMenuResponseModel(ResponseModel[CreateMenuResponseDTO]):
    pass


class ListMenuResponseModel(ResponseModel[List[MenuResponseDTO]]):
    pass


class MenuNullResponseModel(ResponseModel):
    pass
