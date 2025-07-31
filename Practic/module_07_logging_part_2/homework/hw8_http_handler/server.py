import json
from flask import Flask, request


app = Flask(__name__)

all_logs = []

@app.route('/log', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, статус код успешной работы

    """
    logs = request.get_json()

    if not logs:
        return 'We dont have new logs', 400
    
    all_logs.append(logs)
    return 'Logs is saved', 200



@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    if all_logs:
        rendring = "\n".join(json.dumps(log, indent=2, ensure_ascii=False) for log in all_logs)
        return f'<pre>{rendring}</pre>'

if __name__ == '__main__':
    app.run()