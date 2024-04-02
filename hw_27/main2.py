from functools import reduce


def my_func():
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    subtract_three = lambda x: x - 3
    return [add_one, double, subtract_three]


def main(funcs: list, num: float) -> float:
    return reduce(lambda n, func: func(n), funcs, num)


if __name__ == '__main__':
    my_num = 5
    print(main(my_func(), my_num))