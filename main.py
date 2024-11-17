from internal.envs import EnvHandler
from cmd.http.server import HttpServer
from uvicorn import run

EnvHandler.load()

server = HttpServer()
server.setup()
app = server.get_app()

run(app, host="0.0.0.0", port=8000)
