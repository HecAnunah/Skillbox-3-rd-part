"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    allowed_args = {"a", "u", "x", "-f", "-e"}
    try:
        get_args = request.args.getlist("arg", type=str)
        if not all(arg in allowed_args for arg in get_args):
            return "❌ Недопустимый аргумент."

        result = subprocess.run(["ps"] + get_args, capture_output=True, text=True)
        return f"<pre>{result.stdout.strip()}</pre>"
    except Exception as e:
        return f"ERROR: {e}"


if __name__ == "__main__":
    app.run(debug=True)
