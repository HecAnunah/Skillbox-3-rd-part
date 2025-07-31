from ascii_filter import ASCIIFilter

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "filters": {"my_filter": {"()": ASCIIFilter}},
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
            "when": "h",  
            "interval": 5,  
            "backupCount": 2,  
            "encoding": "utf-8",
            "filters": ["my_filter"],
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
