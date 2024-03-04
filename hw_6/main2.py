n = int(input("Введите число N: "))

a, b, count = 0, 1, 0
print("Первые", n, "чисел Фибоначчи:", end=" ")
while count < n:
    print(a, end="")
    if count != n - 1:
        print(", ", end="")
    a, b = b, a + b
    count += 1
