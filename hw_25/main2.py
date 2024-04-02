from pathlib import Path


def file_processing(file: Path) -> list:
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return [line.strip().split() for line in data]
    except FileNotFoundError:
        print('Файл не найден.')


def calculate_total_price(products: list) -> tuple[float, list]:
    total_price = 0.0
    product_list = []

    while products and len(products[0]) >= 3:
        try:
            product_name, price, quantity = products[0][:3]
            total_price += float(price) * int(quantity)
            product_list.append(product_name)
        except ValueError:
            print('Ошибка: Неверный формат данных.')

        products = products[1:]

    return total_price, product_list


def main():
    path = Path('/Users/Openiuk/ICH_HomeWorks/hw_25/products.txt')
    my_list = file_processing(path)

    total_price, product_list = calculate_total_price(my_list)

    return f'Цена {total_price:.2f}, Продукты {product_list}'


if __name__ == '__main__':
    print(main())
