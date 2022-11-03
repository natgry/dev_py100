from pprint import pprint

# TODO решить с помощью list comprehension и распечатать его
pprint([{
    'dec': number,
    'bin': bin(number),
    'oct': oct(number),
    'hex': hex(number)
} for number in range(16)])
