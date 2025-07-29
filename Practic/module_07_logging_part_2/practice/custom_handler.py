import logging
import sys

"""
1. Реализуйте собственный `StreamHandler`: в конструктор он должен принимать поток, с которым будет работать. Если такой не указан — берите `sys.stderr`.
2. Используйте этот обработчик вместо стандартного в конфигурационном файле из прошлой темы. 
3. Попробуйте при вызове какого-нибудь метода логирования передать по ключу `extra` словарь ещё с чем-нибудь. Например:

    ```python
    logger.debug('msg', extra={'very': 'much'})
    ```

    Теперь посмотрите, какие атрибуты есть у этого объекта `LogRecord`. Для этого рекомендуем воспользоваться функцией `vars(record)`.
        
    Как мы это можем использовать? Что будет, если эти атрибуты указать в строке-паттерне Formatter'а? Что будет, если их указать, но не передать в `extra`? 
"""


class myHandler(logging.Handler):
    def __init__(self, stream=None):
        super().__init__()
        self.stream = stream if stream is not None else sys.stderr
        self._stream_name = str(self.stream)

    def emit(self, record: logging.LogRecord) -> None:
        # Добавляем новое поле steam_name
        record.stream_name = self._stream_name
        message = self.format(record)

        # print('Ловим все что есть в рекорд')
        # for key, value in vars(record).items():
        #     print(f'{key}: {value}')
    
        try:
            self.stream.write(message + "\n")
            self.flush()
        except Exception:
            self.handleError(record)

    # Когда ты пишешь в поток (например, sys.stdout, sys.stderr, файл, io.StringIO() и т. д.),
    # данные сначала могут попадать в буфер — временное хранилище в памяти. Это делается для повышения производительности.
    # Метод flush() заставляет поток немедленно записать буферизированные данные в конечную точку (на экран, в файл и т.п.).
    def flush(self) -> None:
        if hasattr(self.stream, "flush"):
            self.stream.flush()


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d || %(stream_name)s +++ %(very)s"
        }
    },
    "handlers": {
        "console": {
            "()": myHandler,
            "stream": sys.stdout,
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
        "with_my_handl": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            # "propagate": False,
        },
    },
    # "filters": {},
    # "root": {} # == "": {}
}
