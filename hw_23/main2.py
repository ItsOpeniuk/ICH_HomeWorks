def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

num = int(input("Enter a number: "))
gen = fibonacci_generator()
for _ in range(num):
    print(next(gen))