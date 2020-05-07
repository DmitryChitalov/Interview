"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение»
из этого пути имени файла (без расширения).
"""
import os


def get_filename(path: str) -> str:
    filename = os.path.basename(path)
    return '.'.join(filename.split('.')[:-1])


def main():
    path = input("Enter path: ")
    filename = get_filename(path)
    print(filename)


if __name__ == '__main__':
    main()
