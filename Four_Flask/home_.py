from typing import List, Optional
from datetime import datetime
from flask import Flask, request, jsonify
import math
import itertools

app = Flask(__name__)


@app.route(
    "/search/",
    methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400
    for call_tower in cell_tower_ids:
        if call_tower <= 0:
            return f"ID cell_tower долэен быть больше 0", 400

    date_from_str = request.args.get("date_from")
    date_to_str = request.args.get("date_to")

    if date_from_str and date_to_str:
        try:
            if date_to_str < date_from_str:
                return "Параметр date_to должен быть позже или равен date_from.", 400

            date_from = datetime.strptime(date_from_str, "%Y%m%d").date()
            date_to = datetime.strptime(date_to_str, "%Y%m%d").date()
        except ValueError:
            return "Неверный формат даты. Используйте YYYYMMDD.", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    for prefix in phone_prefixes:
        if not prefix.endswith("*"):
            return "Префикс должен заканчиваться *", 400
        digits_part = prefix[:-1]  # всё, кроме последнего символа
        if not digits_part.isdigit():
            return "Префикс должен состоять из цифр и заканчиваться *", 400
        if len(digits_part) > 10:
            return "Префикс не должен содержать больше 10 цифр", 400

    protocols: List[str] = request.args.getlist("protocol")
    prot_list = ["2G", "3G", "4G"]
    for prot in protocols:
        if prot not in prot_list:
            return f"Протокол должен быть 2G, 3G или 4G", 400

    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
    )


@app.route("/summ/", methods=["GET"])
def numb_operations():
    numbers: List[int] = request.args.getlist("numb", type=int)
    if not numbers:
        return jsonify({"error": "Пожалуйста, передайте хотя бы одно число."}), 400

    sum_result = sum(numbers)
    prod_result = math.prod(numbers)

    return jsonify({"numbers": numbers, "sum": sum_result, "prod(count)": prod_result})


@app.route("/masiv/", methods=["GET"])
def massiv_operations():
    numbers_a: List[int] = request.args.getlist("numba", type=int)
    numbers_b: List[int] = request.args.getlist("numbb", type=int)

    result = list(itertools.product(numbers_a, numbers_b))
    return result


@app.route("/masnum/", methods=["GET"])
def masnum_operations():
    massive: List[int] = request.args.getlist("mas", type=int)
    number_a = request.args.get("numb", type=int)
    if not massive or number_a is None:
        return jsonify({"error": "Передайте массив a и число x"}), 400

    # Бинарный поиск...
    massive.sort()
    closest = massive[0]
    min_diff = abs(massive[0] - number_a)

    for num in massive[1:]:
        diff = abs(num - number_a)
        if diff < min_diff:
            min_diff = diff
            closest = num

    return jsonify({"needed number in massive A": closest})


if __name__ == "__main__":
    app.run(debug=True)
