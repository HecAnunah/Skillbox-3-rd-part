"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from typing import List
from click import command
from flask import Flask, request
import subprocess
import shlex

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    try:
        get_args: List[str] = request.args.getlist("arg", type=str)
        command = f"ps"

        result = subprocess.run(
            [command] + [arg for arg in get_args], capture_output=True, text=True
        )
        if result.returncode != 0:
            return "Something whent wrong", 500

        return f"<pre>{result.stdout.strip()}</pre>"
    except Exception as e:
        return f"ERROR: {e}"


if __name__ == "__main__":
    app.run(debug=True)
