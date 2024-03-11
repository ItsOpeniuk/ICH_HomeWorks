num = int(input("Enter a num "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{i * j:^3}", end=" ")
    print()