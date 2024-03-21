def calculate(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[key] = (sum(value) / len(value))
    return new_dict


grades = {
    'Alice': [85, 90, 92],
    'Bob': [78, 80, 84],
    'Carol': [92, 88, 95]
}

print(calculate(grades))

