def merge_dicts(**kwargs):

    merged_dict = {}
    for dictionary in kwargs.values():
        for key, value in dictionary.items():
            if key in merged_dict:
                if isinstance(merged_dict[key], list):
                    merged_dict[key].append(value)
                else:
                    merged_dict[key] = [merged_dict[key], value]
            else:
                merged_dict[key] = value
    return merged_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

result = merge_dicts(a=dict1, b=dict2, c=dict3)
print(result)
