from datetime import datetime

from flask import Flask

app = Flask(__name__)

GREETINGS = (
    "Хорошего понедельника",
    "Хорошего вторника",
    "Хорошей среды",
    "Хорошего четверга",
    "Хорошей пятницы",
    "Хорошей субботы",
    "Хорошего воскресенья",
)


@app.route("/hello-world/<name>")
def hello_world(name: str) -> str:
    if len(name.split()) > 1:
        return "Имя должно быть односоставным", 400
    weekday: int = datetime.today().weekday()
    greeting: str = GREETINGS[weekday]
    return f"Привет, {name}. {greeting}!"


if __name__ == "__main__":
    app.run(debug=True)
