input_number = float(input("Введите число с плавающей точкой: "))
sign = -1 if input_number < 0 else 1
integer_part = abs(int(input_number))
fractional_part = abs(input_number) - integer_part

if fractional_part < 0.5:
    rounded_number = integer_part * sign
else:
    rounded_number = (integer_part + 1) * sign

print("Округленное число:", rounded_number)
