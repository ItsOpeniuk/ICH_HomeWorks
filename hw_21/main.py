from collections import Counter

def my_count(string):
    result =  dict(Counter(string.split()))
    max_value = sorted(result.values(), reverse=True)[:2]
    max_key = []
    for key, value in result.items():
        if value in max_value:
            max_key.append((key, value))
    for key, value in max_key:
        print(f'{key}: {value}')




my_count('один два три четыри один один два два два два')