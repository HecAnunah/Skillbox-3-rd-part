"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
 python3 -c 'print("Hellow world!")'
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange
import subprocess

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    cmd = ["prlimit", "--nproc=1:1", "python3", "-c", code]
    proc = subprocess.Popen(
        cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
        return stdout or stderr
    except subprocess.TimeoutExpired:
        proc.kill()
        return f"Ошибка: время выполнения кода истякло."


@app.route("/run_code", methods=["POST"])
def run_code():
    """
    Принимает данные от пользователя, валидирует их и отправляет
    в метод run_python_code_in_subproccess.
    Возвращает строку с результатом работы функции.
    """
    form = CodeForm()
    if form.validate_on_submit():
        code = str(form.code.data)
        timeout = int(form.timeout.data)
        result = run_python_code_in_subproccess(code, timeout)
        return f"{result}"
    return "Ошибка: данные невалидны", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
