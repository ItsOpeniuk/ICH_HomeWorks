def summer():
    my_list = []
    num = input("Enter a number or 'exit' to end the program: ").lower()
    while num != 'exit':
        if num.isdigit():
            my_list.append(int(num))
            num = input("Enter a number or 'exit' to end the program: ").lower()

        else:
            num = input('Incorrect input please Enter a number or "exit" to end the program: ').lower()
    return my_list


print(f'Your dynamic massive is {summer()}')