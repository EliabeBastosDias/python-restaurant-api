from typing import List
from venv import logger

from internal.common.mapper import mapper
from internal.controllers.menu.menu_schema import ListMenuRequestDTO, MenuResponseDTO
from internal.core.domain.menu import Menu
from internal.errors.http_not_found import HttpNotFoundError
from internal.repositories.menu.menu_repo import MenuRepository


class ListMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> List[MenuResponseDTO]:
        self.__menurepository = menurepository

    def execute(self, params: ListMenuRequestDTO):
        logger.info("ListMenuCommand initiated", params)

        entities = self.__search_menus(params=params)

        response = self.__build_response(entities)

        logger.info("ListMenuCommand finished", params)

        return response

    def __search_menus(self, params: ListMenuRequestDTO) -> List[Menu]:
        entities = self.__menurepository.list(
            onlyActives=params.onlyActives, page=params.page
        )
        if len(entities) == 0:
            raise HttpNotFoundError("Menus not found")
        return entities

    def __build_response(self, entities: List[Menu]) -> List[MenuResponseDTO]:
        return list(map(self.__entity_to_dto, entities))

    def __entity_to_dto(self, entity: Menu) -> MenuResponseDTO:
        return mapper.automapping_sqlalchemy_to_pydantic(entity, MenuResponseDTO)
