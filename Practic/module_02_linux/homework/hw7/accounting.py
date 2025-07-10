"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    try:
        dt = datetime.strptime(date, "%Y%m%d")
    except ValueError:
        return f"Некорректная дата: {date}. Формат должен быть YYYYMMDD.", 400

    year = dt.year
    month = dt.month
    day = dt.day

    year_data = storage.setdefault(year, {})
    month_data = year_data.setdefault(month, {})
    month_data[day] = month_data.get(day, 0) + number
    year_data["total"] = year_data.get("total", 0) + number

    return f"Добавлено {number} руб. за {year}.{month:02d}.{day:02d}"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    year_data = storage.get(year)
    if not year_data:
        return f"Нет данных за {year} год"

    year_summ = year_data.get("total")
    return f"Добавлено {year_summ} руб. за {year} год"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    year_data = storage.get(year)
    if not year_data:
        return f"Нет данных за {year} год"

    month_data = year_data.get(month)
    if not month_data:
        return f"Нет данных за {month} месяц"

    totall_month = sum(month_data.values())
    return f"Суммарные траты за указанный год({year}) - {year_data.get('total')}, а за указанный месяц ({month}) - {totall_month}"


if __name__ == "__main__":
    app.run(debug=True)
