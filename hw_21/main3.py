def get_value_from_dict(dictionary: dict, key, method):
    my_dict = dictionary
    my_key = key
    if method == "get":
        return f'Значение для ключа {my_key} - {my_dict.get(my_key, f'Не найдено')}'
    elif method == "set":
        return f'Значение для ключа {my_key} - {my_dict.setdefault(my_key, f' не найдено но мы добавили его в словарь')}'
    else:
        return get_value_from_dict(my_dict, my_key, method=input('Метод должен быть "get" или "set"'))


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
key_input = input('Enter key ')
method = input('if you wont use method "get" write "get",elif you wont use method "setdefault" enter "set" ').lower()
print(get_value_from_dict(my_dict, key_input, method))