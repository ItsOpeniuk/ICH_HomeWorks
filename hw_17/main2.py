def calculate(*args):
    return sum(args)

def main():
    numbers = input("Enter numbers separated by space - ").split()
    numbers = list(map(int, numbers))
    print(calculate(*numbers))


if __name__ == "__main__":
    main()