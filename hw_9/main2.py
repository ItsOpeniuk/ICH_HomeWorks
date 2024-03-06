string = input("Enter you string ").lower().replace(' ', '')
vowels_char = "aeiou"
vowels = ''
consonants = ''
for char in string:
    if char in vowels_char:
        vowels = ''.join(char)
    else:
        consonants = ''.join(char)

print(f'Your string {string} have vowels: {len(vowels)} and consonants: {len(consonants)}')
