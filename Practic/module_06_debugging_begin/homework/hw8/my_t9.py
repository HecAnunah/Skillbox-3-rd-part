"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""

from typing import List

data = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


def my_t9(input_numbers: str) -> List[str]:
    result = []
    with open("words.txt", "r", encoding="utf-8") as f:
        words_list = [word.strip().lower() for word in f.readlines()]

    all_words = [word for word in words_list if len(word) == len(input_numbers)]

    for word in all_words:
        match = True
        for i, char in enumerate(word):
            if char not in data[int(input_numbers[i])]:
                match = False
                break
        if match:
            result.append(word)
    return result

if __name__ == "__main__":
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep="\n")
