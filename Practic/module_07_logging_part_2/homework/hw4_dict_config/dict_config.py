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
    },
    "loggers": {
        "calc": {
            "level": "DEBUG",
            "handlers": ["file"],
            "propagate": False,
        },
        "string_to_operator": {"level": "DEBUG", "handlers": ["file"]},
    },
    # "filters": {},
    # "root": {} # == "": {}
}
