import logging

class DebugHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        print("LogRecord содержит атрибуты:")
        for key, value in vars(record).items():
            print(f"{key}: {value}")

logger = logging.getLogger("example")
logger.setLevel(logging.DEBUG)
logger.addHandler(DebugHandler())

logger.debug("Test", extra={"user_id": 42})