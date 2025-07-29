from typing import List
from itertools import groupby

data = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' ']  # 0 — пробел
}

def decode_t9(pressed: str) -> str:
    result = ""
    # Разбиваем по группам одинаковых цифр
    groups = [''.join(g) for k, g in groupby(pressed) if k != ' ']
    
    for group in groups:
        digit = group[0]
        count = len(group)
        if digit in data:
            letters = data[digit]
            # Если нажали больше, чем длина списка — делаем круг
            index = (count - 1) % len(letters)
            result += letters[index]
    return result

if __name__ == "__main__":
    input_line = input("Введите последовательность кнопок (например: 4433555 555666096667775553):\n")
    print(decode_t9(input_line))