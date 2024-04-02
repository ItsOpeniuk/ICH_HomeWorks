def generator(start, step, finish):
    for i in range(start, finish+1, step):
        yield start
        start += step

def main():
    start = int(input("Enter a starting number: "))
    step = int(input("Enter a number of steps: "))
    finish = int(input("Enter a final number: "))
    gen = generator(start, step, finish)
    for i in gen:
        print(i)


if __name__ == "__main__":
    main()