def calculate_sum_and_product(a, b):
    total_sum = a + b
    product = a * b
    return (total_sum, product)

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result = calculate_sum_and_product(num1, num2)
print(f"Сумма и произведение чисел: {result}")
