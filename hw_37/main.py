import mysql.connector


def process_query(config: dict, table: str):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        print(f'Error while connecting to MySQL: {e}')
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()




if __name__ == "__main__":
    mysql_config = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com', 'user': 'ich1',
'password': 'password', 'database': 'ich_edit'}
    rows = process_query(mysql_config, table='users')
    for row in rows:
        print(row)
