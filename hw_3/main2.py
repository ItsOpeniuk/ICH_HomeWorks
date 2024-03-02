from math import pi

def main(radius):
    print(f'Длина окружности = {2*pi*radius:.2f}')
    print(f'Площадь окружности = {pi*radius**2:.2f}')


if __name__ == '__main__':
    main(float(input('Enter radius: ')))






