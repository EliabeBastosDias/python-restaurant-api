from venv import logger

from internal.controllers.menu.menu_params import InactivateMenuParams


class InactivateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result

    def to_dict(self):
        return {"success": self.success, "result": self.result}


class InactivateMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: InactivateMenuParams):
        try:
            logger.info("InactivateMenuCommand initiated", params)

            entity = self.__menurepository.get(token=params.token, onlyActives=True)
            if entity is None:
                raise Exception("Menu not found")

            self.__menurepository.inactivate(token=params.token)

            logger.info("InactivateMenuCommand finished", params)

            return InactivateMenuResult(success=True, data=entity)
        except Exception as err:
            logger.error("InactivateMenuCommand failed", params, err)

            raise err
