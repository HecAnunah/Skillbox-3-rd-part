import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def human_readable_size(size_bytes):
    # Перевод байт в человекочитаемый формат
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = float(size_bytes)
    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} ПБ"

def insert_file(file):
    """
    Принимает список строк вывода ls -la,
    возвращает кортеж: (кол-во файлов, кол-во папок, суммарный размер файлов в байтах)
    """
    dir_count= 0
    file_count = 0
    total_size = 0

    for line in file:
        parts = line.split()
        if len(parts) < 9:
            continue

        size = parts[4]
        code_naimenovanie = parts[0]

        if code_naimenovanie.startswith('d'):
            dir_count += 1
        else:
            file_count += 1
            total_size += int(size)
    
    return dir_count, file_count, total_size
        

with open('output.txt', 'r', encoding='utf-8') as f:
    research_file = f.readlines()

dir_count, file_count, total_size = insert_file(research_file)

normalize_size = human_readable_size(total_size)

print('Папок: ', dir_count)
print('Файлов: ', file_count)
print('Всего байт: ', total_size)
print('Байт в нормальном виде: ', normalize_size)


