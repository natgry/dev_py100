list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_value = list_numbers[0]
max_index = 0
last_index = len(list_numbers) - 1
last_value = list_numbers[last_index]

for pos, value in enumerate(list_numbers):
    if value > max_value:
        max_value = value
        max_index = pos

for pos, value in enumerate(list_numbers):
    if pos == max_index:
        list_numbers[last_index] = list_numbers[pos]
        list_numbers[pos] = last_value

print(list_numbers)
