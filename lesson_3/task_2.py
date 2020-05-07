"""
 Написать программу, которая запрашивает у пользователя ввод числа.
 На введенное число она отвечает сообщением, целое оно или дробное.
 Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
 Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def alert_type(num):
    if isinstance(num, float):
        print(f"Your number {num} is float type")
        print(comparing_num_parts(num))
    else:
        print(f"Your number {num} is int type")


def comparing_num_parts(num: float):
    whole, fractional = str(num).split('.')
    return whole == fractional


def main():
    alert_type(34)
    alert_type(34.0)
    alert_type(12.12)


if __name__ == '__main__':
    main()
