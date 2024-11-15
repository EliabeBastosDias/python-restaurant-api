class UserController:
    def __init__(self, userrepo) -> None:
        self.__userrepo = userrepo
    
    def list(self):
        self.__userrepo.menu.list()