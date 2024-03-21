def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recursive_sum(n // 10)


def main():
    num = int(input("Enter a number: "))
    print(recursive_sum(num))


if __name__ == "__main__":
    main()