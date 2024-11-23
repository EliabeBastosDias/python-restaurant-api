from venv import logger

from internal.controllers.menu.menu_schema import MenuRequestDTO, MenuResponseDTO
from internal.core.domain.menu import Menu
from internal.errors.http_not_found import HttpNotFoundError
from internal.repositories.menu.menu_repo import MenuRepository


class UpdateMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: MenuRequestDTO, token: str) -> MenuResponseDTO:
        try:
            logger.info("UpdateMenuCommand initiated", params)

            entity = self.__get_related_entities(token)

            builded_entity = self.__enrich_entity(entity, params)

            entity_updated = self.__persist_entities(builded_entity)

            response = self.__build_response(entity_updated)

            logger.info("UpdateMenuCommand finished", params)

            return response
        except Exception as err:
            logger.error("UpdateMenuCommand failed", params, err)

            raise err

    def __get_related_entities(self, token: str) -> Menu:
        entity = self.__menurepository.get(token)
        if entity is None:
            raise HttpNotFoundError("Menu not found")
        return entity

    def __enrich_entity(self, entity: Menu, params: MenuRequestDTO) -> Menu:
        entity.name = params.name
        return entity

    def __persist_entities(self, entity: Menu) -> Menu:
        entity_updated = self.__menurepository.update(entity)
        return entity_updated

    def __build_response(self, entity: Menu) -> MenuResponseDTO:
        return MenuResponseDTO(
            token=entity.token,
            name=entity.name,
            active=entity.active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
