def sum_generator():
    sum = 0
    while True:
        number = yield sum
        if number == 0:
            return sum
        sum += number

if __name__ == "__main__":
    sum_gen = sum_generator()
    next(sum_gen)
    while True:
        try:
            new_number = int(input("Введите число (0 для выхода): "))
            result = sum_gen.send(new_number)
            print(result)
        except StopIteration as e:
            print("Конечная сумма:", e.value)
            break
