from functools import reduce
from itertools import accumulate
from operator import mul

def main(my_list):
    return [reduce(lambda x, y: x * y, my_list), list(accumulate(my_list, mul))]


my_list = [1, 2, 3, 4, 6, 7, 5, 44]
print(main(my_list))