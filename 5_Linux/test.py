from flask import Flask

'''Урок 5.3 Python Advanced для корректной работы нужны файлы stderr.txt и stdout.txt
Команда для запуска из терминала: ython3 -m test  > stdout.txt 2> stderr.txt
'''


# Фласк все принты пишет в stderr по умолчанию. Эта строка для теста файла stdout
print("Привет из stdou")

app = Flask(__name__)

# Перекидываем файл об ошибках ы stderr.txt а остальную инфу в файл stdout.txt


@app.endpoint("test")
def test():
    print("Test >>>>>>> stdou.txt")
    return "test"


if __name__ == "__main__":
    app.add_url_rule("/test", endpoint="test")
    app.run(debug=True)
