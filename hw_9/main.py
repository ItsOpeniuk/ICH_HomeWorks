new_string = input("Enter a message ").lower().replace(' ', '')
alphabet = ('abcdefghijklmnopqrstuvwxyz')
count = 0
for i in new_string:
    if i in alphabet:
        count += 1
    else:
        continue

if count == len(new_string):
    print('String is pangramm ')
else:
    print('String is not pangramm ')
