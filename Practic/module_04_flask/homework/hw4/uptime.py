"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=["GET"])
def uptime() -> str:
    try:
        get_uptime = subprocess.run(["uptime", "-s"], capture_output=True, text=True)
        uptime = get_uptime.stdout.strip()
        return uptime
    except Exception as e:
        return f"Ошибка получения uptime: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
