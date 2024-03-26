def func(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

            num1 = int(lines[0].strip())
            num2 = int(lines[1].strip())

            summa = num1 + num2
            diff = num1 - num2
            multiplication = num1 * num2
            division = num1 / num2
    except FileNotFoundError: print("File not found")
    except ValueError: print("inncorrect format data in file")
    except ZeroDivisionError: print("You can't divide by zero")
    else:
        print(f"{num1} + {num2} = {summa}\n"
              f"{num1} - {num2} = {diff}\n"
              f"{num1} * {num2} = {multiplication}\n"
              f"{num1} / {num2} = {division:.3f}")

my_file = '/Users/Openiuk/ICH_HomeWorks/hw_22/file.txt'
func(my_file)