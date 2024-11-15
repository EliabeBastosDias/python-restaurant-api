from pydantic import BaseModel

class MenuCreateRequest(BaseModel):
    name: str

class MenuUpdateRequest(BaseModel):
    name: str

class MenuRouter:
    def __init__(self, app, menucontroller):
        self.__app = app
        self.__menucontroller = menucontroller

    def setup(self):
        @self.__app.post("/menus")
        def create(body: MenuCreateRequest):
            return self.__menucontroller.create_action(body)

        @self.__app.get("/menus/{menu_token}")
        def get(menu_token):
            return self.__menucontroller.get_action(menu_token)
        
        @self.__app.get("/menus")
        def list(menu_token: str = None, active: bool = False, page: int = 1):
            return self.__menucontroller.list_action(menu_token, active, page)

        @self.__app.put("/menus/{menu_token}")
        def update(body: MenuUpdateRequest, menu_token: str = None):
           return self.__menucontroller.update_action(body,menu_token)

        @self.__app.patch("/menus/{menu_token}/inactivate")
        def inactivate(menu_token: str = None):
            return self.__menucontroller.get_action(menu_token)