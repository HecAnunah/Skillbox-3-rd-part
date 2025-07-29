"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""

from typing import Dict
import json
from collections import Counter
from datetime import datetime


def get_json_string():
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as f:
        for string in f:
            json_string = json.loads(string)
            yield json_string


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    result = {}

    json_file = get_json_string()
    for strin in json_file:
        level = strin["level"]
        if level not in result:
            result[level] = 1
        else:
            result[level] += 1
    return result


def task2() -> str:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    counter = Counter()
    json_file = get_json_string()
    for strin in json_file:
        time = strin.get("time", "")
        hour = time.split(":")[0]
        counter[hour] += 1
    result = counter.most_common(1)[0][0]
    return f"Max count logs {result}"


def task3() -> str:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    counter = Counter()

    json_file = get_json_string()

    for string in json_file:
        start = datetime.strptime("05:00:00", "%H:%M:%S").time()
        end = datetime.strptime("05:20:00", "%H:%M:%S").time()
        time = string.get("time")
        date_time = datetime.strptime(time, "%H:%M:%S").time()

        if start <= date_time <= end:
            errors = string.get("level", "")
            if errors == "CRITICAL":
                counter[errors] += 1
    return f"Критических ошибок за период 05:00:00 по 05:20:00 :  {counter['CRITICAL']}"


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    counter = 0

    json_file = get_json_string()
    for string in json_file:
        msg = string.get("message")
        if "dog" in msg.lower():
            counter += 1
    return counter


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    counter = Counter()

    json_file = get_json_string()
    for string in json_file:
        warning_level = string.get('level')
        if warning_level == 'WARNING':
            words_message = string.get('message')
            words_lst = words_message.lower().split()
            counter.update(words_lst)
    return counter.most_common(1)[0][0]



        


if __name__ == "__main__":
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f"{i}. {task_answer}")
