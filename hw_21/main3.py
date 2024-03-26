def get_value_from_dict(dictionary: dict, key, method):
    if method == "get":
        return f'Значение для ключа {key} = {dictionary.get(key, f'Key {key} not found')}'
    elif method == "set":
        return f'Значение для ключа {key} = {dictionary.setdefault(key, f'Key {key} not found but we invite his in your dictionary')}'
    else:
        return input('You entered incorrect method')


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
key_input = input('Enter key ')
method = input('if you wont use method "get" write "get",elif you wont use method "setdefault" enter "set" ').lower()
print(get_value_from_dict(my_dict, key_input, method))