def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n -1)


def main():
    num = int(input("Enter a number: "))
    print(factorial(num))


if __name__ == "__main__":
    main()