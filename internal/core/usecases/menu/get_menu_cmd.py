from venv import logger

from internal.controllers.menu.menu_schema import GetMenuRequestDTO, MenuResponseDTO
from internal.core.domain.menu import Menu
from internal.repositories.menu.menu_repo import MenuRepository


class GetMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: GetMenuRequestDTO) -> MenuResponseDTO:
        try:
            logger.info("GetMenuCommand initiated", params)

            entity = self.__search_menu(params=params)

            response = self.__build_response(entity)

            logger.info("GetMenuCommand finished", params)
            return response
        except Exception as err:
            logger.error("GetMenuCommand failed", params, err)

            raise err

    def __search_menu(self, params: GetMenuRequestDTO) -> Menu:
        entity = self.__menurepository.get(token=params.token)
        if entity is None:
            raise Exception("Menu not found")
        return entity

    def __build_response(self, entity: Menu) -> MenuResponseDTO:
        return MenuResponseDTO(
            token=entity.token,
            name=entity.name,
            active=entity.active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
