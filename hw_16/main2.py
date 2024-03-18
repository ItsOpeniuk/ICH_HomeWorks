def main():

    input_str = input("Введите список чисел через пробел: ")
    input_list = [int(x) for x in input_str.split()]
    input_list.sort(reverse=True)
    print(f"Отсортированный список в порядке убывания: {input_list}")


if __name__ == "__main__":
    main()
