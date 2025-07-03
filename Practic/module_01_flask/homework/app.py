import datetime
import random
from flask import Flask
import os
import re

app = Flask(__name__)

cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cats = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин",
]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")
with open(BOOK_FILE, "r", encoding="utf-8") as f:
    text = f.read()
words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)


class Counter:
    def __init__(self):
        self.counter = 0

    def visits(self):
        self.counter += 1
        return self.counter


counter = Counter()


@app.route("/hello_world")
def test_function():
    return f"Hello, world!"


@app.route("/cars")
def test_cars():
    global cars
    return f"Cars new pages in brows. We have a new cars, brands: {', '.join(cars)}."


@app.route("/cats")
def test_cats():
    global cats
    choise_response = random.choice(cats)
    return f"Вы больше всего соответствуете: {choise_response}"


@app.route("/get_time/now")
def test_get_time():
    time = datetime.datetime.now()
    return "Время сейчас: " + str(time)


@app.route("/get_time/future")
def test_future_time():
    time_now = datetime.datetime.now()
    current_time_after_hour = time_now + datetime.timedelta(hours=1)
    return f"Точное время через час будет: {current_time_after_hour}"


@app.route("/get_random_word")
def test_get_random_word():
    global words
    random_word = random.choice(words)
    return f"Рандомное слово из книги Льва Толстого: {random_word}"


@app.route("/counter")
def test_counter():
    global counter
    count = counter.visits()
    return str(count)


if __name__ == "__main__":
    app.run(debug=True)
