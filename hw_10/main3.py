string = input("Enter a string: ")

new_string = ''
unique_chars = []
for char in string:
    if char not in unique_chars:
        unique_chars.append(char)
    else:
        if char not in new_string:
            new_string += ','+char
if new_string:
    print(f'symbols {new_string.strip(',')} repeat')
else:
    print('all symbols in string are unique')
