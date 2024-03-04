number = int(input("Введите целое положительное число: "))

is_prime = True
divisor = 2
while divisor < number:
    if number % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print(number, "является простым числом")
else:
    print(number, "не является простым числом")
