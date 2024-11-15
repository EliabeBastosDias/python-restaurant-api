from venv import logger

from internal.core.domain.menu import Menu


class GetMenuParams:
    def __init__(self, token) -> None:
        self.token = token

class GetMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result
    
    def to_dict(self):
        return {
            "success": self.success,
            "result": self.result
        }

class GetMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params):
        try:
            logger.info("GetMenuCommand initiated", params)

            entity = self.__menurepository.get(token=params.token)
            if entity == None:
                raise Exception("Menu not found")

            logger.info("GetMenuCommand finished", params)

            return GetMenuResult(success=True, data=entity)
        except Exception as err:
            logger.error("GetMenuCommand failed", params, err)

            raise err
    