number = int(input("Enter a number: "))
original_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10
if reverse_number == original_number:
    print("The number is polindrome")
else:
    print("The number is not polindrome")



