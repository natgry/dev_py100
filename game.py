from math import sqrt
import os
from typing import Union

"""
0 - пустая клетка
1 - клетка занята первым игроком
2 - клетка занята вторым игроком

Пример пустого поля:
    [0, 0, 0,
    0, 0, 0,
    0, 0, 0]

"""

ROLE_INT = {0: " ",
            1: "0",
            2: "X"}

ROLE_CHAR = {"0": 1,
             "X": 2}


def get_role_char(val: int) -> Union[str, None]:
    return ROLE_INT.get(val, None)


def get_role_int(val: str) -> Union[int, None]:
    return ROLE_CHAR.get(val, None)


def clear_console():
    os.system('cls')


def play_game(field: list, who_starts: int) -> None:
    """
    Реализует ход игры.
    :param field: игровое поле
    :param who_starts: игрок, который ходит первым.
    :return:
    """
    who_goes = who_starts

    while not all(who_win(field)) and found_empty_cells(field):
        draw_field(field)

        while True:
            user_choice = input(f"Ход для игрока {get_role_char(who_goes)}. "
                                    f"Введите индекс ячейки игрового поля\n")
            try:
                assert user_choice
            except AssertionError:
                print(f"Введено пустое значение")
                draw_field(field)
                continue

            user_choice = int(user_choice)

            try:
                assert user_choice < len(field)
            except AssertionError:
                print(f"Ячейка {user_choice} не существует.")
                draw_field(field)
                continue

            try:
                assert is_cell_empty(field, user_choice)
            except AssertionError:
                print(f"Ячейка {user_choice} занята.")
                draw_field(field)
                continue
            else:
                break

        field[user_choice] = who_goes
        draw_field(field)
        who_goes = get_role_int("0") if who_goes == get_role_int("X") else get_role_int("X")
        clear_console()


def draw_field(field: list) -> None:
    """
    Функция рисует в консоль состояние поля
    Пусть: 0 - пустое поле " "
          1 - нолик "O"
          2 - крестик "X"


    Пример пустого поля:
      [0, 0, 0,
      0, 0, 0,
      0, 0, 0]
    В консоле

    | | | |
    | | | |
    | | | |

    Пример поля:
      [2, 0, 2,
      0, 1, 0,
      0, 0, 1]

    |Х| |Х|
    | |O| |
    | | |O|


    :param field:
    :return:
    """

    print("Ваше игровое поле:")
    row_width = round(sqrt(len(field)))
    for i in range(0, len(field), row_width):
        cells = field[i:i + row_width]
        draw_line = '|'
        for cell in cells:
            draw_line += get_role_char(cell) + '|'
        print(draw_line)


def get_win_positions(field: list) -> list[list]:
    """
    Функция формирует выйгрышные позиции на игровом поле.
    :param field: игровое поле
    :return: список выйгрышных позиций на игровом поле
    """

    row_width = round(sqrt(len(field)))

    # строки
    rows = []
    for i in range(0, len(field), row_width):
        rows.append(field[i:i + row_width])

    # колонки
    cols = list(zip(*rows))

    # диагонали
    diag_left = []
    diag_right = []
    for i, row in enumerate(rows):
        diag_left.append(row[i])
        diag_right.append(row[-1 - i])

    return [*rows, *cols, diag_left, diag_right]


def found_empty_cells(field: list) -> bool:
    """
    Функция проверяет, есть ли еще пустые ячейки в поле
    :param field: игровое поле
    :return: есть ли еще пустые ячейки в поле, True - есть, False - пустых ячеек нет
    """

    return not all(field)


def is_cell_empty(field: list, index: int) -> bool:
    """
    Функция проверяет, свободна ли ячейка игрового поля.
    :param field: игровое поле
    :param index: индекс ячейки
    :return: свободна ли ячейка, True - ячейка свободна, False - ячейка занята
    """

    return field[index] == 0


def who_win(field: list) -> (int, int):
    """
    Функция определяет кто выйграл в игре. При максимальной неразрывной последовательности длиной размером поля.

    пусть (a, b) - a: 0 - игра ещё идет
                      1 - игра закончена
                  b: 0 - никто не победил или ничья
                     1 - первый
                     2 - второй

    Пример пустого поля:
      [0, 0, 0,
      0, 0, 0,
      0, 0, 0]

     (0, 0)

    Пример поля:
      [2, 0, 2,
      0, 1, 0,
      0, 0, 1]

    (0, 0)

    Пример поля:
      [2, 1, 2,
      1, 1, 2,
      2, 1, 1]

    (1, 1)

    Пример поля:
      [1, 1, 2,
      1, 1, 2,
      2, 2, 1]

    (1, 0)


    :param field:
    :return: возвращает кортеж значений (a, b): a - означает закончена ли игра.
      b - означает кто выйграл.
    """
    game_over = False
    winner = 0

    for row in get_win_positions(field):
        if all([i == 1 for i in row]):
            game_over = True
            winner = 1
            print(f"Игра закончена. Выйграли: {get_role_char(winner)}")
            return game_over, winner
        if all([i == 2 for i in row]):
            game_over = True
            winner = 2
            print(f"Игра закончена. Выйграли: {get_role_char(winner)}")
            return game_over, winner

    if not found_empty_cells(field):
        game_over = True
        winner = 0
        print("Игра закончена. Никто не победил или ничья")
        return game_over, winner

    print("Игра ещё идет.")
    return game_over, winner


def test_who_win():
    field_game_not_over_no_winner = [0, 1, 0, 2, 0, 0, 1, 0, 0]
    res = who_win(field_game_not_over_no_winner)
    assert res == (0, 0), res

    field_row_winner = [0, 1, 0, 1, 1, 1, 1, 2, 2]
    res = who_win(field_row_winner)
    assert res == (1, 1), res

    field_column_winner = [0, 2, 0, 1, 2, 1, 1, 2, 2]
    res = who_win(field_column_winner)
    assert res == (1, 2), res

    field_diag_winner = [2, 0, 0, 0, 2, 1, 1, 2, 2]
    res = who_win(field_diag_winner)
    assert res == (1, 2), res

    field_diag_winner = [0, 0, 1, 0, 1, 2, 1, 2, 2]
    res = who_win(field_diag_winner)
    assert res == (1, 1), res

    field_no_winner = [1, 2, 1, 1, 1, 2, 2, 1, 2]
    res = who_win(field_no_winner)
    assert res == (1, 0), res

    field_row_winner = [1, 1, 0, 1, 0, 0, 1, 0, 2, 2, 2, 2, 1, 0, 1, 1]
    res = who_win(field_row_winner)
    assert res == (1, 2), res

    field_column_winner = [1, 1, 2, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    res = who_win(field_column_winner)
    assert res == (1, 1), res

    field_diag_winner = [2, 1, 2, 2, 1, 2, 0, 1, 0, 2, 2, 0, 1, 1, 1, 2]
    res = who_win(field_diag_winner)
    assert res == (1, 2), res


def test_found_empty_cells():
    """
    Функция тестирует found_empty_cells()
    :return:
    """
    field = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    assert found_empty_cells(field)

    field = [1, 2, 1, 1, 1, 1, 2, 2, 2]
    assert not found_empty_cells(field)


def test_get_win_positions():
    """
    Функция тестирует get_field_win_positions().
    :return:
    """
    list_ = get_win_positions([0, 0, 0, 1, 1, 1, 2, 2, 2])
    assert (list_[0] == [0, 0, 0] and list_[1] == [1, 1, 1] and list_[2] == [2, 2, 2]), \
        "Проверяем строки"
    assert (list_[3] == (0, 1, 2) and list_[4] == (0, 1, 2) and list_[5] == (0, 1, 2)), \
        "Проверяем колонки"
    assert list_[6] == [0, 1, 2], "Проверяем левую диагональ"
    assert list_[7] == [0, 1, 2], "Проверяем правую диагональ"

    list_ = get_win_positions([0, 0, 1, 1, 1, 1, 2, 2, 0])
    assert (list_[0] == [0, 0, 1] and list_[1] == [1, 1, 1] and list_[2] == [2, 2, 0]), \
        "Проверяем строки"
    assert (list_[3] == (0, 1, 2) and list_[4] == (0, 1, 2) and list_[5] == (1, 1, 0)), \
        "Проверяем колонки"
    assert list_[6] == [0, 1, 0], "Проверяем левую диагональ"
    assert list_[7] == [1, 1, 2], "Проверяем правую диагональ"

    list_ = get_win_positions([2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
    assert (list_[0] == [2, 2, 2, 2] and list_[1] == [1, 1, 1, 1]
            and list_[2] == [0, 0, 0, 0] and list_[3] == [1, 1, 1, 1]), \
        "Проверяем строки"
    assert (list_[4] == (2, 1, 0, 1) and list_[5] == (2, 1, 0, 1)
            and list_[6] == (2, 1, 0, 1) and list_[7] == (2, 1, 0, 1)), \
        "Проверяем колонки"

    assert list_[8] == [2, 1, 0, 1], "Проверяем левую диагональ"
    assert list_[9] == [2, 1, 0, 1], "Проверяем правую диагональ"

    list_ = get_win_positions([2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 1, 1])
    assert (list_[0] == [2, 2, 2, 1] and list_[1] == [1, 1, 1, 1]
            and list_[2] == [0, 0, 0, 0] and list_[3] == [2, 1, 1, 1]), \
        "Проверяем строки"
    assert (list_[4] == (2, 1, 0, 2) and list_[5] == (2, 1, 0, 1)
            and list_[6] == (2, 1, 0, 1) and list_[7] == (1, 1, 0, 1)), \
        "Проверяем колонки"
    assert list_[8] == [2, 1, 0, 1], "Проверяем левую диагональ"
    assert list_[9] == [1, 1, 0, 2], "Проверяем правую диагональ"


def test_draw_field() -> None:
    """
    Функция тестирует draw_field().

    :return:
    """
    # 3 x 3
    draw_field([0, 1, 1, 1, 0, 0, 2, 2, 2])
    draw_field([1, 1, 1, 0, 0, 0, 2, 2, 2])
    draw_field([1, 0, 0, 0, 1, 0, 2, 2, 1])
    draw_field([2, 0, 2, 0, 2, 0, 2, 1, 1])
    draw_field([0] * 9)
    draw_field([1] * 9)
    draw_field([2] * 9)
    # 4 x 4
    draw_field([2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
    draw_field([1] * 16)


def test_is_cell_empty() -> None:
    """
    Функция тестирует is_cell_empty().

    :return:
    """
    field = [0, 1, 1, 1, 0, 0, 2, 2, 2]
    assert is_cell_empty(field, 0)
    assert not is_cell_empty(field, 1)


def test_helpers():
    test_get_win_positions()
    test_found_empty_cells()
    test_who_win()
    test_draw_field()
    test_is_cell_empty()


def main():
    run_test = int(input("Запустить тесты? 1 - да, 0 - нет\n "))
    if run_test:
        print("Запускаем тесты...")
        test_helpers()
        print("Тесты прошли успешно")
        clear_console()

    player_1 = None
    while player_1 not in [1, 2]:
        role = input("Выберите роль первого игрока: X или 0\n ")
        player_1 = get_role_int(role)
    player_2 = 1 if player_1 == 2 else 2
    print(f"Роль второго игрока: {get_role_char(player_2)}")

    row_width = -1
    while row_width < 2:
        row_width = int(input("Выберите ширину игрового поля: [2, 3, 4, ..]\n"))
    field = [0] * row_width ** 2
    draw_field(field)

    play_game(field, who_starts=player_1)


if __name__ == "__main__":
    main()
