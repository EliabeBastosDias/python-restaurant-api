from venv import logger

from internal.core.domain.menu import Menu


class CreateMenuParams:
    def __init__(self, name) -> None:
        self.name = name

class CreateMenuResult:
    def __init__(self, success, result) -> None:
        self.success = success
        self.result = result
    
    def to_dict(self):
        return {
            "success": self.success,
            "result": self.result
        }

class CreateMenuCommand:
    def __init__(self, menurepository) -> None:
        self.__menurepository = menurepository

    def execute(self, params):
        try:
            logger.info("CreateMenuCommand initiated", params)

            self.__check_if_menu_already_exists(params)
            
            builded_menu = self.__build_menu(params)
            
            created_entity = self.__persist_entities(builded_menu)

            logger.info("CreateMenuCommand finished", params)

            return CreateMenuResult(success=True, data=created_entity)
        except Exception as err:
            logger.error("CreateMenuCommand failed", params, err)

            raise err
    
    def __check_if_menu_already_exists(self, params):
        existingMenu = self.__menurepository.getByName(params.name)
        if existingMenu != None:
            raise Exception("Menu already exists")
        
    def __build_menu(self, params):
        builded_menu = Menu
        builded_menu.name = params.name
        return builded_menu

    def __persist_entities(self, builded_menu):
        return self.__menurepository.insert(builded_menu)