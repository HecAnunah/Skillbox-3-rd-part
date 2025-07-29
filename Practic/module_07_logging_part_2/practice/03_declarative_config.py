import logging
import logging.config


"""
## 7.3

* Перепишите практику из прошлого урока на декларативный манер
* Добавьте в конфиг еще один обработчик: `FileHandler` с уровнем `DEBUG`. Используйте уже созданный Formatter.
* Добавьте этот обработчик к логгерам `sub_1`, `sub_2`.
"""


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logfile.log",
            "mode": "a",
        },
    },
    "loggers": {
        "new": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            # "propagate": False,
        },
        "sub_1": {"level": "DEBUG", "handlers": ["file", "console"]},
        "sub_2": {"level": "DEBUG", "handlers": ["file", "console"]},
    },
    # "filters": {},
    # "root": {} # == "": {}
}

logging.config.dictConfig(dict_config)
logger = logging.getLogger("new")

sub1 = logging.getLogger("sub_1")
sub2 = logging.getLogger("sub_2")
print(sub1.handlers)


# Проверяем что пишет лог файл
sub1.debug("ddddd")
