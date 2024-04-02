def square(x):
    return (i ** 2 for i in range(1, x+1))


num = int(input('Enter a number: '))
for s in square(num):
    print(s)
