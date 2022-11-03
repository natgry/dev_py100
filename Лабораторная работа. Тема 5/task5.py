import string
from random import sample


# TODO написать функцию генерации случайных паролей
def get_random_password(n: int = 8) -> str:
    chars = [string.ascii_uppercase, string.ascii_lowercase, string.digits]
    password = sample("".join(chars), k=n)
    return "".join(password)


print(get_random_password())
