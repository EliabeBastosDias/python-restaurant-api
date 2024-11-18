from venv import logger

from internal.controllers.menu.menu_params import CreateMenuParams
from internal.core.domain.menu import Menu
from internal.repositories.menu_repo import MenuRepository


class CreateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result

    def to_dict(self):
        return {"success": self.success, "result": self.result}


class CreateMenuCommand:
    def __init__(self, menurepository: MenuRepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params: CreateMenuParams):
        try:
            logger.info("CreateMenuCommand initiated", params)

            self.__check_if_menu_already_exists(params)

            builded_menu = self.__build_menu(params)

            created_entity = self.__persist_entities(builded_menu)

            logger.info("CreateMenuCommand finished", params)

            return CreateMenuResult(success=True, result=created_entity)
        except Exception as err:
            logger.error("CreateMenuCommand failed", params, err)

            raise err

    def __check_if_menu_already_exists(self, params: CreateMenuParams):
        existingMenu = self.__menurepository.getByName(params.name)
        if existingMenu is not None:
            raise Exception("Menu already exists")

    def __build_menu(self, params: CreateMenuParams):
        builded_menu = Menu(**params.__dict__)
        return builded_menu

    def __persist_entities(self, builded_menu: Menu):
        return self.__menurepository.insert(builded_menu)
