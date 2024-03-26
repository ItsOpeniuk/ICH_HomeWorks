class MyValuEerror(Exception): pass


def calculate(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        num1 = int(lines[0].strip())
        num2 = int(lines[1].strip())

        if (num1 / num2) < 0:
            raise MyValuEerror()


    except FileNotFoundError: print("Файл не найден")
    except MyValuEerror: print('Результат не может быть отрицательным')
    except ValueError:
        print('Данные с файла не удалось преобразовать в тип "int"')
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    else:
        result = num1 / num2
        print(f'Result: {result:.4f}')


my_file = '/Users/Openiuk/ICH_HomeWorks/hw_22/file.txt'
calculate(my_file)
