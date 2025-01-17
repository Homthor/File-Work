def custom_write(file_name: str, strings):
    # Создаем пустой словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл в режиме записи с указанием кодировки utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        line_number = 1
        for string in strings:
            # Получаем текущую позицию
            start_position = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, start_position)] = string
            line_number += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
