"""
Удобно сохранять логи в определённом формате, чтобы затем их можно было фильтровать и анализировать.
Сконфигурируйте логгер так, чтобы он писал логи в файл skillbox_json_messages.log в следующем формате:

{"time": "<время>", "level": "<уровень лога>", "message": "<сообщение>"}

Но есть проблема: если в message передать двойную кавычку, то лог перестанет быть валидной JSON-строкой:

{"time": "21:54:15", "level": "INFO", "message": "“"}

Чтобы этого избежать, потребуется LoggerAdapter. Это класс из модуля logging,
который позволяет модифицировать логи перед тем, как они выводятся.
У него есть единственный метод — process, который изменяет сообщение или именованные аргументы, переданные на вход.

class JsonAdapter(logging.LoggerAdapter):
  def process(self, msg, kwargs):
    # меняем msg
    return msg, kwargs

Использовать можно так:

logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Сообщение')

Вам нужно дописать метод process так, чтобы в логах была всегда JSON-валидная строка.
"""

import logging
import json


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        new_message = json.dumps(msg, ensure_ascii=False)
        return new_message, kwargs


if __name__ == "__main__":
    logger = JsonAdapter(logging.getLogger(__name__))
    logger.setLevel(logging.DEBUG)

    log_file_handler = logging.FileHandler(
        "skillbox_json_messages.log", encoding="utf-8"
    )
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    log_file_handler.setFormatter(formatter)
    logger.logger.addHandler(log_file_handler)

    logger.info("Сообщение")
    logger.error('Кавычка)"')
    logger.debug("Еще одно сообщение")

    with open("skillbox_json_messages.log", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            parts = line.strip().split(" - ", 2)
            if len(parts) < 3:
                print("Не валидная строка")

            json_part = parts[2]
            try:
                json.loads(json_part)
                print("JSON валиден")
            except Exception:
                print("JSON не валиден.")
