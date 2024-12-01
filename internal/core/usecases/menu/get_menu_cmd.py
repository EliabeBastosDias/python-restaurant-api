from venv import logger

from internal.common.mapper import mapper
from internal.controllers.menu.menu_schema import GetMenuRequestDTO, MenuResponseDTO
from internal.core.domain.menu import Menu
from internal.errors.http_not_found import HttpNotFoundError
from internal.repositories.menu.menu_repo import MenuRepository


class GetMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: GetMenuRequestDTO) -> MenuResponseDTO:
        logger.info("GetMenuCommand initiated", params)

        entity = self.__search_menu(params=params)

        response = self.__build_response(entity)

        logger.info("GetMenuCommand finished", params)
        return response

    def __search_menu(self, params: GetMenuRequestDTO) -> Menu:
        entity = self.__menurepository.get(token=params.token)
        if entity is None:
            raise HttpNotFoundError("Menu not found")
        return entity

    def __build_response(self, entity: Menu) -> MenuResponseDTO:
        return mapper.automapping_sqlalchemy_to_pydantic(entity, MenuResponseDTO)
