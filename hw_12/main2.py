a = input('Enter first string: ')
b = input('Enter second string')
my_list = []
for i, j in zip(a, b):
    my_list.append((i, j))

print(my_list)