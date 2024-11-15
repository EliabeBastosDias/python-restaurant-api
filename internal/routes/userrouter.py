class UserRouter:
    def __init__(self, app, usercontroller):
        self.__app = app
        self.__usercontroller = usercontroller

    def setup(self):
        @self.__app.get("/menus")
        def list(request, response):
            return self.__usercontroller.list(request, response)

        @self.__app.get("/menus/{menu_token}")
        def get(request, response):
            return self.__usercontroller.get(request, response)