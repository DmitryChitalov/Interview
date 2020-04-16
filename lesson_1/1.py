'''
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком,
который формируется в цикле. После этого осуществляется вызов внешней
lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции. Элементы строки
(элементы таблицы умножения) должны разделяться табуляцией.
'''


def print_tab(num_col: int, num_row: int):
    for row in range(1, num_row + 1):
        for col in range(1, num_col + 1):
            # print((lambda x, y: str(x * y) + ' ' * (4 - len(str(x * y))))(row, col), end='')
            print((lambda x, y: str(x * y) + '\t')(row, col), end='')
        print()


if __name__ == '__main__':
    print_tab(20, 20)
