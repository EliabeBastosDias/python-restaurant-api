from venv import logger

from internal.core.domain.menu import Menu


class UpdateMenuParams:
    def __init__(self, token, name) -> None:
        self.token = token
        self.name = name

class UpdateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result
    
    def to_dict(self):
        return {
            "success": self.success,
            "result": self.result
        }

class UpdateMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params):
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
    
    def __get_related_entities(self, params):
        entity = self.__menurepository.get(token=params.token)
        if entity == None:
            raise Exception("Menu not found")
        return entity
    
    def __enrich_entity(self, entity, params):
        entity.name = params.name
        return entity
    
    def __persist_entities(self, entity):
        self.__menurepository.update(entity)