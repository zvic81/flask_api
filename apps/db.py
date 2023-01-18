import psycopg2
from config import host, user, password, db_name, port


def connect_db(host=host, user=user, password=password, db_name=db_name):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port
        )
    except psycopg2.OperationalError:
        print('Error: No BD server ready, try one more')
        return 0
    connection.autocommit = True
    return connection


# select * records from db and return list
def select_all_goods_db() -> list:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute("SELECT id, name FROM goods ORDER BY id;")
        cnt = g.fetchall()
        goods = []
        for row in cnt:
            goods.append({'id': row[0], 'name': row[1], })
        close_db(connection)
        return goods


# select all orders from db, return list of dictionaries
def select_all_orders_db() -> list:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute(
            "SELECT id, order_date, customer_name, customer_email, delivery_address, status, notes FROM orders ORDER BY id;")
        cnt = g.fetchall()
        orders = []
        for row in cnt:
            orders.append({
                'id': row[0],
                'order_date': row[1],
                'customer_name': row[2],
                'customer_email': row[3],
                'delivery_address': row[4],
                'status': row[5],
                'notes': row[6],
            })
        close_db(connection)
        return orders


# select id record from db and return dict
def select_id_good_db(id: int) -> dict:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute(
            "SELECT id,name,price,manufacture_date,picture_url FROM goods WHERE id=%s;", (id,))
        cnt = g.fetchone()
        goods = {}
        goods['id'] = cnt[0]
        goods['name'] = cnt[1]
        goods['price'] = cnt[2]
        goods['manufacture_date'] = cnt[3]
        goods['picture_url'] = cnt[4]
        close_db(connection)
        return goods


# insert new good into db
def insert_good_db(good_list: dict) -> list:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute("""
                    INSERT INTO goods (name, price, manufacture_date, picture_url)
        VALUES (%s,%s,%s,%s);""", (good_list.get('name'), good_list.get('price'), good_list.get('manufacture_date'), good_list.get('picture_url')))
        g.execute("SELECT id FROM goods ORDER BY id DESC LIMIT 1;")
        cnt = g.fetchone()
    close_db(connection)
    return cnt[0]


def insert_order_db(order_list: dict) -> int:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute("""
                INSERT INTO orders (order_date, customer_name, customer_email, delivery_address, status, notes)
                VALUES (%s,%s,%s,%s,%s,%s);""", (order_list.get('order_date'), order_list.get('customer_name'), order_list.get('customer_email'),
                                                 order_list.get('delivery_address'), 'new_ord', order_list.get('notes')))
        g.execute("SELECT id FROM orders ORDER BY id DESC LIMIT 1;")
        cnt = g.fetchone()
        goods = order_list.get('good_item')
        for item in goods:
            g.execute("""
                     INSERT INTO order_item (ammount, notes, order_id, good_id)
                     VALUES (%s,%s,%s,%s);""", (item.get('ammount'), 'notes null', cnt[0], item.get('good_id')))
    close_db(connection)
    return cnt[0]  # return id new order


def update_id_good_db(id: int, good_list: dict) -> int:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute("SELECT COUNT(id) FROM goods WHERE id=%s", (id,))
        cnt = g.fetchone()
        if not cnt[0]:
            close_db(connection)
            return 0
        g.execute("""
                    UPDATE goods SET name=%s,price=%s,manufacture_date=%s,
                    picture_url=%s WHERE id=%s;""", (good_list.get('name'), good_list.get('price'), good_list.get('manufacture_date'), good_list.get('picture_url'), id))
    close_db(connection)
    return 1


def delete_id_good_db(id: int) -> str:
    connection = connect_db()
    with connection.cursor() as g:
        g.execute("""DELETE FROM goods WHERE id=%s;""", (id,))
    close_db(connection)
    return g.statusmessage


def close_db(connection: any) -> None:
    if connection:
        connection.close()
