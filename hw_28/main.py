def func(add_list: list) -> list:
    return list(map(lambda x : x.upper(), [word for word in add_list if word[0].lower() in 'aeiou']))

my_list = ['apple', 'banana', 'coconut', 'esse']

print(func(my_list))