from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

from models import Base, Goods, Orders, Order_item
import config

engine = create_engine(
    f'postgresql+psycopg2://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}:{config.DATABASE_PORT}/{config.DATABASE_NAME}',
    pool_pre_ping=True, echo=False)

Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
db_session = session_factory()
logger = logging.getLogger('db')


def select_all_goods_db():
    goods = db_session.query(Goods.id, Goods.name).all()
    return goods


def select_all_orders_db(user_email: str):
    orders = db_session.query(Orders).filter(
        Orders.customer_email == user_email).all()
    return orders


def select_id_good_db(id: int):
    goods = db_session.query(Goods).filter(Goods.id == id).one()
    return goods


def insert_good_db(good_list: dict):
    good = Goods(**good_list)
    db_session.add(good)
    db_session.commit()
    return good.id


def insert_order_db(order_list: dict):
    good_items = order_list.pop('good_item')
    order = Orders(**order_list)
    db_session.add(order)
    db_session.flush()
    for g in good_items:
        good = Order_item(**g, order_id=order.id, notes='temp')
        db_session.add(good)
    db_session.commit()
    return order.id


def update_id_good_db(id: int, good_list: dict):
    good = db_session.query(Goods).get(id)
    for key, value in good_list.items():
        setattr(good, key, value)
    db_session.add(good)
    db_session.commit()
    return good.id


def delete_id_good_db(id: int) -> str:
    c = db_session.query(Goods).filter(Goods.id == id)
    if not db_session.query(c.exists()).scalar():
        return -1
    res = db_session.query(Goods).filter(Goods.id == id).delete()
    db_session.commit()
    return res


def init_db():
    cnt = db_session.query(Goods).count()
    if not cnt:
        db_session.add_all([
            Goods(name='Beer', price=112,
                  manufacture_date='05/07/22', picture_url='pic112'),
            Goods(name='Mushrooms', price=12,
                  manufacture_date='05/07/22', picture_url='pic1/mush'),
            Goods(name='keyboard', price=3,
                  manufacture_date='05/07/20', picture_url='keyb1/c'),
            Goods(name='iphone', price=345,
                  manufacture_date='05/07/15', picture_url='apple.com'),
            Goods(name='mouse', price=5, manufacture_date='05/01/12',
                  picture_url='mouse.com'),
        ])
        db_session.add_all([
            Orders(order_date='02/05/2014', customer_name='Sekretov',
                   customer_email='secret@mail.ru', delivery_address='Apatity', status='new', notes='ww'),
            Orders(order_date='02/05/2015', customer_name='Mihrin', customer_email='mihrin@mail.ru',
                   delivery_address='kirovsk', status='temp', notes='aas'),
            Orders(order_date='02/05/2031', customer_name='Zelenskyi',
                   customer_email='zelo@mail.ru', delivery_address='Kyiev', status='ready', notes=' '),
            Orders(order_date='02/05/2022', customer_name='Karlson', customer_email='karlson@mail.ru',
                   delivery_address='Stohgolm', status='reset', notes='ee'),
            Orders(order_date='02/05/2021', customer_name='Ivan', customer_email='ivan@n.r',
                   delivery_address='prostokvash', status='deliv', notes='sas'),
        ])
        db_session.commit()
        good1 = db_session.query(Goods).filter(Goods.name == 'keyboard').one()
        orders1 = db_session.query(Orders).filter(
            Orders.customer_name == 'Sekretov').one()
        oi1 = Order_item(ammount=3, notes='notesss')
        oi1.goods = good1
        oi1.orders = orders1
        db_session.add(oi1)
        db_session.commit()


init_db()
