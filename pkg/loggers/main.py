import traceback
import logging
import http.client as http_client


class LoggerHandler:
    def __init__(self) -> None:
        http_client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        self.logger = logging.getLogger("MenuApi")
        self.logger.setLevel(logging.INFO)
        self.set_logs()
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str, exception: Exception) -> None:
        self.logger.error(f"{message}: {exception}")
        self.logger.error(traceback.format_exc())

    def set_logs(self) -> None:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)