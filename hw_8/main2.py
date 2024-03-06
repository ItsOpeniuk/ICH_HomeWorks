number = int(input("Enter a number: "))

original_number = number
count = 0
summ = 0

while number != 0:
    digit = number % 10
    summ += digit ** 3
    count += 1
    number //= 10

if summ == original_number:
    print("This number is an Armstrong Number")
else:
    print("This number is not an Armstrong Number")
