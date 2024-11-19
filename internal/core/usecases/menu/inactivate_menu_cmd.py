from venv import logger

from internal.controllers.menu.menu_schema import InactivateMenuRequestDTO
from internal.repositories.menu.menu_repo import MenuRepository






class InactivateMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: InactivateMenuRequestDTO) -> None:
        try:
            logger.info("InactivateMenuCommand initiated", params)

            entity = self.__menurepository.get(token=params.token, onlyActives=True)
            if entity is None:
                raise Exception("Menu not found")

            self.__menurepository.inactivate(token=params.token)

            logger.info("InactivateMenuCommand finished", params)

        except Exception as err:
            logger.error("InactivateMenuCommand failed", params, err)

            raise err
