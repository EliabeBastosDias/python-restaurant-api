from venv import logger

from internal.controllers.menu.menu_schema import (
    InactivateMenuRequestDTO,
)
from internal.core.domain.menu import Menu
from internal.repositories.menu.menu_repo import MenuRepository


class InactivateMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: InactivateMenuRequestDTO) -> None:
        try:
            logger.info("InactivateMenuCommand initiated", params)

            entity = self.__search_menu(params)

            self.__inactivate_menu(entity)

            logger.info("InactivateMenuCommand finished", params)

        except Exception as err:
            logger.error("InactivateMenuCommand failed", params, err)
            raise err

    def __search_menu(self, params: InactivateMenuRequestDTO) -> Menu:
        entity = self.__menurepository.get(token=params.token, onlyActives=True)
        if entity is None:
            raise Exception("Menu not found")
        return entity

    def __inactivate_menu(self, entity: Menu) -> Menu:
        entity_inactivated = self.__menurepository.inactivate(entity.token)
        return entity_inactivated
