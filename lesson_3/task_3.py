"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и
значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Значения,
которым не хватило ключей, необходимо отбросить.
"""
from random import randrange


def generate_two_not_equals_lists():
    while True:
        list_a = [randrange(10, 100) for _ in range(randrange(1, 10))]
        list_b = [randrange(10, 100) for _ in range(randrange(1, 10))]
        if len(list_a) != len(list_b):
            return list_a, list_b


def main():
    result_dict = {}
    list_keys, list_values = generate_two_not_equals_lists()
    for i in range(len(list_keys)):
        try:
            result_dict.update({list_keys[i]: list_values[i]})
        except IndexError:
            result_dict.setdefault(list_keys[i], None)

    print(f"keys: {list_keys}")
    print(f"values: {list_values}")
    print(result_dict)


if __name__ == '__main__':
    main()
