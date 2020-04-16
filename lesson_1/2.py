import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    dir_list = os.listdir(sPath)
    file_list = list()
    dir_list = list()
    get_files = lambda x: (elem for elem in os.listdir(x) if os.path.isfile(os.path.join(x, elem)))
    get_dirs = lambda x: (elem for elem in os.listdir(x) if os.path.isdir(os.path.join(x, elem)))



if __name__ == '__main__':
    print_directory_contents('/home/user/Downloads')
