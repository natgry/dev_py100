list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
sum_ = sum(set(list_))
print(sum_)

count_ = len(set(list_))
print(count_)

avg_ = round(sum_ / count_, 5)
print(avg_)