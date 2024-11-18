from internal.envs.envs import EnvHandler, EnvKey
from cmd.http.server import HttpServer
from uvicorn import run


EnvHandler.load()

server = HttpServer()
server.setup()
app = server.get_app()

run(app, host="0.0.0.0", port=EnvHandler.get_int(EnvKey.SERVER_PORT))
