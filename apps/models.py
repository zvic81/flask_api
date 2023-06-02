from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP, VARCHAR, REAL, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()


class Goods(Base):
    __tablename__ = 'goods'
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    name = Column(VARCHAR(40), nullable=False)
    price = Column(REAL, nullable=False)
    manufacture_date = Column(Date, default=datetime.now, nullable=True)
    picture_url = Column(VARCHAR(100), nullable=True)
    order_item = relationship("Order_item")


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    order_date = Column(Date, default=datetime.now, nullable=False)
    customer_name = Column(VARCHAR(40), nullable=False)
    customer_email = Column(VARCHAR(40), nullable=True)
    delivery_address = Column(VARCHAR(50), nullable=True)
    status = Column(VARCHAR(50), nullable=True)
    notes = Column(VARCHAR(50), nullable=True)
    order_item = relationship("Order_item")


class Order_item(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    ammount = Column(Integer, nullable=False)
    notes = Column(VARCHAR(10), nullable=True)
    order_id = Column(ForeignKey(
        'orders.id', ondelete='CASCADE'), nullable=False, index=True)
    good_id = Column(ForeignKey('goods.id', ondelete='CASCADE'),
                     nullable=False, index=True)
    orders = relationship("Orders")
    goods = relationship("Goods")
