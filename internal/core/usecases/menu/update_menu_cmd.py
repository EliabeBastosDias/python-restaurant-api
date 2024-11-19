from venv import logger

from internal.controllers.menu.menu_schema import MenuRequestDTO
from internal.core.domain.menu import Menu
from internal.repositories.menu.menu_repo import MenuRepository


class UpdateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result

    def to_dict(self):
        return {"success": self.success, "result": self.result}


class UpdateMenuCommand:
    def __init__(self, menurepository:MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: MenuRequestDTO, token: str):
        try:
            logger.info("UpdateMenuCommand initiated", params)

            entity = self.__get_related_entities(token)

            builded_entity = self.__enrich_entity(entity, params)

            self.__persist_entities(builded_entity)

            logger.info("UpdateMenuCommand finished", params)

            return UpdateMenuResult(success=True, data=entity)
        except Exception as err:
            logger.error("UpdateMenuCommand failed", params, err)

            raise err

    def __get_related_entities(self, token: str):
        entity = self.__menurepository.get(token)
        if entity is None:
            raise Exception("Menu not found")
        return entity

    def __enrich_entity(self, entity, params: MenuRequestDTO):
        entity.name = params.name
        return entity

    def __persist_entities(self, entity: Menu):
        self.__menurepository.update(entity)
