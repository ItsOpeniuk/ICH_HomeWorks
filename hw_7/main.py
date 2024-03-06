number = int(input("Enter a number: "))
my_str = ''

while number > 0:
    digit = number % 2
    my_str += str(digit)
    number = number // 2

print(int(my_str[::-1]))
