import getpass
import hashlib
import logging
import re

logger = logging.getLogger("new_logger")


def input_and_check_password():
    logger.debug("Начало работы с функцией input_and_chek_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Необходимо заполнить поле пароля.")
        return False

    pattern = r"""^(?=.*[a-z])        # хотя бы одна строчная
               (?=.*[A-Z])        # хотя бы одна заглавная
               (?=.*\d)           # хотя бы одна цифра
               (?=.*[!@#$%^&*()\-=+_])  # хотя бы один спецсимвол
               .{8,}$             # не менее 8 символов
            """

    regex = re.compile(
        pattern, re.VERBOSE
    )  # Флаг re.VERBOSE позволяет читать регулярные выражения с комментариями

    if not bool(regex.match(password)):
        logger.warning(
            "В пароле должна быть 1 строчная буква, 1 латинская и спецсимвол. Минимум 8 знаков!"
        )
        return False

    try:
        hashing = hashlib.md5()
        logger.debug("Мы создали объект hashing")

        hashing.update(password.encode("utf-8"))

        logger.debug("В объект hashing добавлен password")

        if hashing.hexdigest() == "d2a9b166d58f67fdffff80e71b85e566":
            logger.debug("Аутентификация пользователя пройденна")
            return True

    except ValueError as ex:
        logger.exception(f"Вы ввели некорректный символ", exc_info=ex)

    logger.debug("Аутентификация не пройденна.")
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    logger.info("Для аутентификации на сервере введите пароль.")
    try:
        choice_count = int(
            input("Сколько раз вы хотите попытаться ввести пароль (Max=10, min=2): ")
        )
        if 2 < choice_count < 10:
            logger.info(f"У вас есть {choice_count} попыток")
        else:
            logger.warning("Указан не верный диапазон: минимум 2 максимум 10 попыток.")
            exit(1)

    except ValueError as exc:
        logger.exception("Не верный формат ввода колличества попыток. Введите число.")
        exit(1)

    for _ in range(choice_count):
        if input_and_check_password():
            exit(0)

    logger.error(f"Пользователь ввел пароль неверно {choice_count} раза")

    exit(1)
