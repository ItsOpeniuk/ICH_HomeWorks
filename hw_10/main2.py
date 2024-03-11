string = input("Enter you text please ")
vowels_char = "aeiou"
result = ''
for char in string:
    if char in vowels_char:
        continue
    else:
        result += ''.join(char)
print(result)
