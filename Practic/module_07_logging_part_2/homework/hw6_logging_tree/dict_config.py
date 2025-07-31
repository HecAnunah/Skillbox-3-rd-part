dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "file": {
            "()": "logger_helper.LevelFileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename_err": "calc_error.log",
            "filename_debug": "calc_debug.log",
            "mode": "a",
        },
        "file_utils": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "utils.log",
            "when": "h",          # часы
            "interval": 5,        # раз в 5 час
            "backupCount": 2,    # хранить 2 последних файлов = 10 часов
            "encoding": "utf-8"
        },
    },
    "loggers": {
        "calc": {
            "level": "DEBUG",
            "handlers": ["file"],
            "propagate": False,
        },
        "utils": {"level": "INFO", "handlers": ["file_utils"]},
    },
}
