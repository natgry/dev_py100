def get_count_char(str_):
    chars = dict()
    for char in str_.lower():
        if char.isalpha():
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    return chars


def get_count_char_percent(dict_):
    chars = dict()
    all_chars = sum(dict_.values())
    for char in dict_.keys():
        chars[char] = round((dict_[char] / all_chars * 100), 2)
    return chars


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_count_char_percent(get_count_char(main_str)))
