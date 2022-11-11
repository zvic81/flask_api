# not for use, test
def connect_db(connection, host, user, password, db_name):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True


# select * records from db and return list
def select_all_db(connection: any) -> list:
    with connection.cursor() as g:
        g.execute("SELECT id, name FROM goods ORDER BY id;")
        cnt = g.fetchall()
        goods = []
        for row in cnt:
            good = {
                'id': row[0],
                'name': row[1],
            }
            goods.append(good)
        return goods

#  select all orders from db, return list of dictionaries


def select_all_orders_db(connection: any) -> list:
    with connection.cursor() as g:
        g.execute(
            "SELECT id, order_date, customer_name, customer_email, delivery_address, status, notes FROM orders ORDER BY id;")
        cnt = g.fetchall()
        orders = []
        for row in cnt:
            order = {
                'id': row[0],
                'order_date': row[1],
                'customer_name': row[2],
                'customer_email': row[3],
                'delivery_address': row[4],
                'status': row[5],
                'notes': row[6],
            }
            orders.append(order)
        return orders


# select id records from db and return list
def select_id_db(connection: any, id: int) -> list:
    with connection.cursor() as g:
        g.execute("SELECT * FROM goods WHERE id=%s;", (id,))
        cnt = g.fetchall()
        goods = []
        for row in cnt:
            good = {
                'id': row[0],
                'name': row[1],
                'price': row[2],
                'manufacture_date': row[3],
                'picture_url': row[4]
            }
            goods.append(good)
        return goods

# insert new good into db


def insert_db(connection: any, good_list: list) -> tuple:
    with connection.cursor() as g:
        g.execute("""
                    INSERT INTO goods (name,price,manufacture_date,picture_url)
    VALUES (%s,%s,%s,%s);""", (good_list[0], good_list[1], good_list[2], good_list[3]))
        g.execute("SELECT id FROM goods ORDER BY id DESC LIMIT 1;")
        cnt = g.fetchone()
    return cnt

# update goods where id


def update_id_db(connection: any, id: int, good_list: list) -> int:
    with connection.cursor() as g:
        g.execute("SELECT COUNT(id) FROM goods WHERE id=%s", (id,))
        cnt = g.fetchone()
        if not cnt[0]:
            return 0
        g.execute("""
                    UPDATE goods SET name=%s,price=%s,manufacture_date=%s,
                    picture_url=%s WHERE id=%s;""", (good_list[0], good_list[1], good_list[2], good_list[3], id))
    return 1

# delete good=id


def delete_id_db(connection: any, id: int) -> str:
    with connection.cursor() as g:
        g.execute("""
                    DELETE FROM goods WHERE id=%s;""", (id,))
    return g.statusmessage


def close_db(connection: any) -> None:
    if connection:
        connection.close()
        print("<connection closed>")
