import mysql.connector


def get_connection(config: dict):
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print('Error while connecting to MySQL:', err)


def get_user_names(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, name FROM users')
            return cursor.fetchall()
    except mysql.connector.Error as err:
        print('Error while fetching user names:', err)


def get_user_purchases(connection, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT users.name, product.prod, product.quantity 
                              FROM sales
                              RIGHT JOIN users ON sales.id = users.id
                              RIGHT JOIN product ON sales.pid = product.pid
                              WHERE users.id = %s''', (user_id,))
            return cursor.fetchall()
    except mysql.connector.Error as err:
        print('Error while fetching user purchases:', err)


def print_user_names(names):
    count = 0
    for user_id, user_name in names:
        print(f'id - {user_id} name - {user_name}', end=', ')
        count += 1
        if count % 10 == 0:
            print()
    print()


def main():
    config = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
              'user': 'ich1', 'password': 'password', 'database': 'ich_edit'}

    connection = get_connection(config)
    if connection:
        user_names = get_user_names(connection)
        if user_names:
            print_user_names(user_names)
            user_id = int(input('Select user id: '))
            user_purchases = get_user_purchases(connection, user_id)
            if user_purchases:
                print(user_purchases)
        connection.close()


if __name__ == '__main__':
    main()
