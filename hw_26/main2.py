import os
# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории
# и выводит список всех файлов и поддиректорий внутри этой директории. Для этой задачи используйте модуль os и его
# функцию walk. Программа должна выводить полный путь к каждому файлу и директории.

def func(pach):
     return os.walk(pach)


if __name__ == '__main__':
    path = '/Users/Openiuk/ICH_HomeWorks'
    for item in (func(path)):
        absolut_path = os.path.abspath(item[0])
        print(absolut_path)