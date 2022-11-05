from random import randint


def get_unique_list_numbers() -> list[int]:
    set_ = set()
    start = -10
    stop = 10
    count = 15
    while len(set_) < count:
        set_.add(randint(start, stop))

    return list(set_)  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
