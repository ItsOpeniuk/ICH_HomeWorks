def reversed(string):
    my_list = string.split(' ')
    return ' '.join(my_list[::-1])

my_string = 'Hello from the server'

print(reversed(my_string))