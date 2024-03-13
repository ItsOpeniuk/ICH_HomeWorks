def func(string):
    return tuple(len(x) for x in string.split(' '))

string = 'Some string with some numbers'
print(func(string))