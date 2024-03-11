user_string = input("Введите строку: ")
width = int(input("Введите ширину: "))

if len(user_string) >= width:
    aligned_string = user_string
else:
    left_offset = (width - len(user_string)) // 2
    aligned_string = user_string.center(width)
    if (width - len(user_string)) % 2 != 0:
        aligned_string = user_string.rjust(width - left_offset)

print(aligned_string)
