dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "HTTP": {
            "()": "httpHandler.JSHTTPHandler",
            "level": "DEBUG",
            "formatter": "base",
            "host": "localhost:5000",
            "url": "/log",
            "method": "POST",
        },
    },
    "loggers": {"server": {"level": "DEBUG", "handlers": ["HTTP"], "propagate": False}},
}
