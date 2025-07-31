import logging
import logging.config
import sys
from dict_config import dict_config
from logging_tree import tree
from logging_tree import format

class LevelFileHandler(logging.Handler):
    def __init__(
        self, filename_err="calc_error.log", filename_debug="calc_debug.log", mode="a"
    ):
        super().__init__()
        self.filename_err = filename_err
        self.filename_debug = filename_debug
        self.mode = mode
        self.stream = sys.stdout

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        try:
            if record.levelno == logging.DEBUG:
                try:
                    with open(self.filename_debug, self.mode, encoding="utf-8") as f:
                        f.write(message + "\n")
                except Exception:
                    self.handleError(record)

            elif record.levelno == logging.ERROR:
                try:
                    with open(self.filename_err, self.mode, encoding="utf-8") as f:
                        f.write(message + "\n")
                except Exception:
                    self.handleError(record)

            else:
                self.stream.write(message + "\n")
                self.stream.flush()
        except Exception:
            self.handleError(record)


def get_logger(name):
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger(name)

    trees = tree()

    with open("logging_tree.txt", "w", encoding="utf-8") as f:
        f.write(format.build_description(trees))

    return logger
