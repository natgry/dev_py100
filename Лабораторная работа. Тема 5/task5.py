from string import ascii_uppercase, ascii_lowercase, digits
from random import sample


# TODO написать функцию генерации случайных паролей
def get_random_password(n: int = 8) -> str:
    password = sample(ascii_uppercase + ascii_lowercase + digits, k=n)
    return "".join(password)


print(get_random_password())
