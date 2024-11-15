from venv import logger

from internal.core.domain.menu import Menu


class InactivateMenuParams:
    def __init__(self, token) -> None:
        self.token = token

class InactivateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result
    
    def to_dict(self):
        return {
            "success": self.success,
            "result": self.result
        }

class InactivateMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params):
        try:
            logger.info("InactivateMenuCommand initiated", params)

            entity = self.__menurepository.get(token=params.token, onlyActives=True)
            if entity == None:
                raise Exception("Menu not found")

            self.__menurepository.inactivate(token=params.token)

            logger.info("InactivateMenuCommand finished", params)

            return InactivateMenuResult(success=True, data=entity)
        except Exception as err:
            logger.error("InactivateMenuCommand failed", params, err)

            raise err
    