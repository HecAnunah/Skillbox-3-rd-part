import logging


root_logger = logging.getLogger()


sub1_logger = logging.getLogger("sub_1")
sub2_logger = logging.getLogger("sub_2")
# Запрещаем передавать данные родителю
sub2_logger.propagate = False

sub_sub_1_logger = logging.getLogger("sub_2.sub_sub_1")

# Handler - обработчик
log_handler = logging.StreamHandler()
log_handler.setLevel(logging.DEBUG)

# Formatter: `<имя логера> || <уровень> || <сообщение> || <модуль>.<имя функции>:<номер строки>`
log_formatter = logging.Formatter(
    fmt="%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d"
)
log_handler.setFormatter(log_formatter)

# Добавляем обработчик в логгер
sub1_logger.addHandler(log_handler)
sub_sub_1_logger.addHandler(log_handler)

# Создайте для логгера обработчик `root` с уровнем `DEBUG` и уже созданным Formatter.
root_handler = logging.StreamHandler()
root_handler.setLevel(logging.DEBUG)
root_handler.setFormatter(log_formatter)
root_logger.addHandler(root_handler)

def main():
    print("Root logger:")
    print(root_logger.handlers)

    print("Sub1:")
    print(sub1_logger.handlers)

    print("sub2:")
    print(sub2_logger.handlers)

    print("sub_sub1:")
    print(sub_sub_1_logger.handlers)

    sub_sub_1_logger.debug("Hi there!")


if __name__ == "__main__":
    main()
