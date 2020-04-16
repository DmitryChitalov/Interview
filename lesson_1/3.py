"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны
создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random


def rand_gen(min_num, max_num):
    result_dict = {}
    result_list = []
    # Так как в условии ничего не сказано о размере словаря, то делаю размерность до 100 элементов
    for i in range(100):
        key = f'elem_{i + 1}'
        val = random.randrange(min_num, max_num)
        if val == 0:
            continue
        result_dict[key] = val
        result_list.append(val)
    print(f'Dict: {result_dict}\nList: {result_list}')


if __name__ == '__main__':
    rand_gen(-10, 10)
