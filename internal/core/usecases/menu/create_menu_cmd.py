from venv import logger

from internal.common.mapper import mapper
from internal.controllers.menu.menu_schema import (
    CreateMenuResponseDTO,
    MenuRequestDTO,
)
from internal.core.domain.menu import Menu
from internal.errors.http_bad_request import HttpBadRequestError
from internal.repositories.menu.menu_repo import MenuRepository


class CreateMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: MenuRequestDTO) -> CreateMenuResponseDTO:
        try:
            logger.info("CreateMenuCommand initiated", params)

            self.__check_if_menu_already_exists(params)

            builded_menu = self.__build_menu(params)

            entity = self.__persist_entities(builded_menu)

            response = self.__build_response(entity)

            logger.info("CreateMenuCommand finished", params)
            return response
        except Exception as err:
            logger.error("CreateMenuCommand failed", params, err)

            raise err

    def __check_if_menu_already_exists(self, params: MenuRequestDTO):
        existingMenu = self.__menurepository.getByName(params.name)
        if existingMenu is not None:
            raise HttpBadRequestError("Menu already exists")

    def __build_menu(self, params: MenuRequestDTO) -> Menu:
        builded_menu = mapper.automapping_pydantic_to_sqlalchemy(params, Menu)
        return builded_menu

    def __persist_entities(self, builded_menu: Menu) -> Menu:
        created_entity = self.__menurepository.insert(builded_menu)
        return created_entity

    def __build_response(self, created_entity: Menu) -> CreateMenuResponseDTO:
        menu_dto = mapper.automapping_sqlalchemy_to_pydantic(
            created_entity, CreateMenuResponseDTO
        )
        return menu_dto
