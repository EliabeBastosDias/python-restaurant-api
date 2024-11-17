from venv import logger

from internal.controllers.menu.menu_params import ListMenuParams


class ListMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result

    def to_dict(self):
        return {"success": self.success, "result": self.result}


class ListMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: ListMenuParams):
        try:
            logger.info("ListMenuCommand initiated", params)

            entities = self.__menurepository.list(
                onlyActives=params.onlyActives, page=params.page
            )
            if len(entities) == 0:
                raise Exception("Menus not found")

            logger.info("ListMenuCommand finished", params)

            return ListMenuResult(success=True, data=entities)
        except Exception as err:
            logger.error("ListMenuCommand failed", params, err)

            raise err