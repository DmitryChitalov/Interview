import os


def exchange_numbers(row: str):
    # Заменяет значение в идущее в начале строки (число) на такое же текстовое в конце строки

    num, phrase = row.split(' ')
    return ' '.join([phrase, phrase + '\n'])


def read_file(path):
    # Возвращает текст, из указанного файла

    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def rewrite_file(path, text):
    # Записывает в указанный файл переданный текст

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('File was re-writen')


def main():
    filename = input("Enter filename for re-writing: ")
    new_text_list = []
    path = os.path.abspath(filename)
    if os.path.exists(path):
        old_text_lines = read_file(path).split('\n')
        for line in old_text_lines:
            new_text_list.append(exchange_numbers(line))
    rewrite_file(path, ''.join(new_text_list))


if __name__ == '__main__':
    main()
