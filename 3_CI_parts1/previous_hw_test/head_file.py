from typing import List
import flask
import os

app = flask.Flask(__name__)


@app.route("/head/<filename>")
def give_summ(filename: str):
    if not os.path.exists(filename):
        return "Файл не найден", 404
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            if not text.strip():
                return "Файл пустой", 400
            return "".join(text), 200
    except (UnicodeDecodeError, StopIteration):
        return "Не удалось прочитать файл", 400


if __name__ == "__main__":
    app.run(debug=True)
