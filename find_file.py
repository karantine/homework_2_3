import os

current_dir = os.path.dirname(os.path.abspath(__file__))
migrations = os.path.join(current_dir, "../Migrations")

def filter_files(target_path):
    sqlfiles = []
    for f in os.listdir(target_path):
        if os.path.isfile(os.path.join(target_path, f)):
            if os.path.splitext(f)[1] == '.sql':
                sqlfiles.append(os.path.join(target_path, f))
    found_file_names = sqlfiles
    while True:
        file_part = input('Введите строку: ')
        filtered = []
        for filename in found_file_names:
            with open(filename) as f:
                text = f.read()
                if file_part in text:
                    filtered.append(filename)
        print('Найденные файлы: {}'.format(filtered))
        print('Всего файлов: {}'.format(len(filtered)))
        if len(filtered) <= 1:
            break
        found_file_names = filtered

filter_files(migrations)

