enter_test_word = [
    "абра-кадабра.",
    "абраа..-кадабра",
    "абраа..-.кадабра",
    "абра....кадабра",
    "абрау...-кадабра",
    "абра........",
    "абр......a.",
    "1..2.3",
    ".",
    "1.......................",
]


def even_odd(enter_list):
    even_list = []
    odd_list = []
    for word in enter_list:
        if word.count(".") % 2 == 0:
            even_list.append(word)
            continue
        odd_list.append(word)
    return even_list, odd_list


even_lst, odd_lst = even_odd(enter_test_word)

print(even_lst.split())
print(odd_lst)
