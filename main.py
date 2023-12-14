import os

filename = 'text.txt'
abs_path = os.path.abspath(__file__)
print(abs_path)

dir_path = os.path.dirname(abs_path)
print(dir_path)

file_path = os.path.join(dir_path,'ppka',filename)
print(file_path)

try:
    f = open(file_path, encoding='utf-8').read(10)
    print(f)
except FileNotFoundError:
    print('Файл не знайдено')
