def func(*args):
    summa = sum(args)
    minimum = min(args)
    maximum = max(args)

    return summa, maximum, minimum
#Можно было без этого блока, но мне было нечего делать )
how_many = int(input("How many numbers you wont invite? "))
result = []
for i in range(1, how_many+1):
    num = int(input(f"Enter a number {i}: "))
    result.append(num)
    how_many -= 1

res = func(*result)
print(f"Сумма чисел = {res[0]} Минимальное значение = {res[1]}, Максимальное значение = {res[2]}")

