from venv import logger

from internal.controllers.menu.menu_schema import ListMenuRequestDTO





class ListMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: ListMenuRequestDTO):
        try:
            logger.info("ListMenuCommand initiated", params)

            entities = self.__menurepository.list(
                onlyActives=params.onlyActives, page=params.page
            )
            if len(entities) == 0:
                raise Exception("Menus not found")

            logger.info("ListMenuCommand finished", params)

        except Exception as err:
            logger.error("ListMenuCommand failed", params, err)

            raise err
