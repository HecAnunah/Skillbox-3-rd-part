"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

2. К нам пришли сотрудники отдела безопасности и сказали, что, согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, является ли пароль хорошим по новым стандартам безопасности.
"""

import getpass
import hashlib
import logging
from nltk.corpus import words
import nltk
import re

nltk.download("words")
logger = logging.getLogger("password_checker")


def is_strong_password(password: str) -> bool:
    english_word = set(words.words())
    lower_password = password.lower()
    clean_password = re.sub(r"[^a-z]", "", lower_password)

    for word in english_word:
        if len(word) >= 3 and word in clean_password:
            logger.warning("Пароль содержит английское слово!")
            return False
    logger.info("Пароль проходит по условиям СБ")
    return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        logger.debug("Функция <is_strong_password> вернула True")

    try:
        hasher = hashlib.md5()
        logger.debug("Создали объект <hasher>")
        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            logger.info("Successful entrance to the system.")
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename="stderr.txt",
        filemode="w",
        encoding="utf-8",
        format="%(asctime)s %(message)s",
        datefmt="%H:%M:%S",
    )
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)
