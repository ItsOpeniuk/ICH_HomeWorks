def sum_generator():

  sum = 0
  while True:
    number = int(input("Введите число: "))
    if number == 0:
      yield sum
      break
    sum += number
    yield sum


if __name__ == "__main__":
    sum_generator = sum_generator()
    for number in sum_generator:
        print(number)