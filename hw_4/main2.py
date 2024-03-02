input1 = input("Введите первое логическое значение (True или False): ").lower()
input2 = input("Введите второе логическое значение (True или False): ").lower()

first = input1 == 'true'
second = input2 == 'true'

print(f'Результат логического И: {first and second}')
print(f'Результат логического ИЛИ: {first or second}')
print(f'Результат логического НЕ (для первого значения): {not first}')
print(f'Результат логического НЕ (для второго значения): {not second}')
print(f'Результат сравнения на равенство: {first == second}')
print(f'Результат сравнения на неравенство: {first != second}')
