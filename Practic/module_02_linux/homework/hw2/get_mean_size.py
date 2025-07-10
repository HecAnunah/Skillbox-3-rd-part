"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_mean_size(ls_output: str) -> float:
    lines = ls_output.strip().split("\n")[1:]
    size_lst = []

    for line in lines:
        parts = line.split()

        if parts[0].startswith("d"):
            continue
        try:
            new_size = int(parts[4])
            size_lst.append(new_size)
        except Exception:
            continue

    if not size_lst:
        return 0.0

    result = sum(size_lst) / len(size_lst)
    return result


if __name__ == "__main__":
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(f"Средний размер файла в каталоге {mean_size}")
