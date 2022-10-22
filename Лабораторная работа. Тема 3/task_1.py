src = not False and True or False and not True

# result = True and True or False and False  # избавляемся от отрицаний
# result = True or False  # избавляемся от логического "и"
# result = True # избавляемся от логического "или"

result = True  # TODO подставить результат выражения

print(src == result)
