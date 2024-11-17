from venv import logger

from internal.controllers.menu.menu_params import UpdateMenuParams
from internal.core.domain.menu import Menu


class UpdateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result

    def to_dict(self):
        return {"success": self.success, "result": self.result}


class UpdateMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: UpdateMenuParams):
        try:
            logger.info("UpdateMenuCommand initiated", params)

            entity = self.__get_related_entities(params)

            builded_entity = self.__enrich_entity(entity, params)

            self.__persist_entities(builded_entity)

            logger.info("UpdateMenuCommand finished", params)

            return UpdateMenuResult(success=True, data=entity)
        except Exception as err:
            logger.error("UpdateMenuCommand failed", params, err)

            raise err

    def __get_related_entities(self, params: UpdateMenuParams):
        entity = self.__menurepository.get(token=params.token)
        if entity is None:
            raise Exception("Menu not found")
        return entity

    def __enrich_entity(self, entity, params: UpdateMenuParams):
        entity.name = params.name
        return entity

    def __persist_entities(self, entity: Menu):
        self.__menurepository.update(entity)
