from functools import reduce
# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел
# из списка, используя функциональные подходы (например, map, filter и reduce).
#
# Пример вывода:
#
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
#
# Результат: 72

def calculate_square(list):
    return reduce(lambda x, y: x + y ** 2, filter(lambda y: y % 2 == 0, list), 0)


if __name__ == '__main__':
    my_list = [4, 6, 3, 4, 2, 3, 9, 0, 7]
    print(calculate_square(my_list))