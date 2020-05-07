import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    for elem in os.listdir(sPath):
        if os.path.isdir(elem):
            new_path = os.path.join(sPath, elem)
            print_directory_contents(new_path)
        else:
            print(elem)


if __name__ == '__main__':
    print_directory_contents('/home/user/Downloads')
