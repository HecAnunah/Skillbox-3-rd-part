import logging
import json
import logging.config
from logging.handlers import HTTPHandler
from dict_config import dict_config
import urllib.request


class JSHTTPHandler(HTTPHandler):
    def mapLogRecord(self, record):
        # Формируем словарь для отправки
        log_record = {
            "name": record.name,
            "level": record.levelname,
            "pathname": record.pathname,
            "lineno": record.lineno,
            "msg": record.getMessage(),
            "created": record.created,
        }
        return log_record

    def emit(self, record):

        try:
            data = json.dumps(self.mapLogRecord(record)).encode("utf-8")
            req = urllib.request.Request(
                url="http://localhost:5000/log",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                response.read()
        except Exception:
            self.handleError(record)


def get_logger(name):
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger(name)

    return logger
