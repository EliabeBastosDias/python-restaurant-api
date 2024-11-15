from internal.envs import EnvHandler
from cmd.http.server import HttpServer

EnvHandler.load()

server = HttpServer()
server.setup()
app = server.get_app()