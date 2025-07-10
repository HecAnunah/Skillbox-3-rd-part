"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

/head_file/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/head_file/12/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

from flask import Flask
import os

app = Flask(__name__)

os.chdir(os.path.dirname(os.path.abspath(__file__)))


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    path = (
        "/home/zakhar/Python/Skillbox third part/Practic/module_02_linux/homework/hw6/"
    )
    full_path = os.path.join(path, relative_path, "test.txt")

    if not os.path.exists(full_path):
        return f"Путь к файлу не найден 404"

    with open(full_path, "r", encoding="utf-8") as f:
        text = f.read()
        text_first = (
            f"Размер файла в символах: {len(text)}. Полный путь к файлу: {full_path}"
        )
        text_second = text[:size]

    return f"{text_first}<br><br><pre>{text_second}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
