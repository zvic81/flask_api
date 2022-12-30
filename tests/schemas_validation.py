# schemas for validation data from db. Using in test_db.py and plugin pytest_schema
import datetime


short_good_schema = {
    "id": int,
    "name": str
}
short_goods_schema = [short_good_schema]

full_good_schema = {
    "id": int,
    "name": str,
    "price": float,
    "manufacture_date": datetime.date,
    "picture_url": str
}

order_schema = {
    "id": int,
    "customer_name": str,
    "delivery_address": str,
    "notes": str,
    "order_date": datetime.date,
    "status": str
}
orders_schema = [order_schema]
