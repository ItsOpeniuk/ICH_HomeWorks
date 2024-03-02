def year(year):
    return 'Високосный' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  else 'Не високосный'


if __name__ == '__main__':
    print(year(int(input('Enter a year '))))