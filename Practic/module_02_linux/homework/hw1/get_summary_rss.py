"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

import os


def human_readable_size(size_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(size_bytes)
    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} ПБ"


def get_summary_rss(ps_output_file_path: str) -> str:
    tottal_size = 0

    file = os.path.join(ps_output_file_path, "output_file.txt")
    with open(file, "r", encoding="utf-8") as f:
        text = f.readlines()

    for line in text:
        print(line)
        split_line = line.split()
        bytes_size = split_line[5]
        if bytes_size.isdigit():
            tottal_size += int(bytes_size)

    return human_readable_size(tottal_size)


if __name__ == "__main__":
    path: str = (
        "/home/zakhar/Python/Skillbox third part/Practic/module_02_linux/homework/hw1/"
    )
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
