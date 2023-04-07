# schemas for validation data from db. Using in test_db.py and test_api_mock.py. Need installed plugin "pip install pytest_schema"
import datetime
from pytest_schema import Or


short_good_schema = {
    "id": int,
    "name": str
}
short_goods_schema = [short_good_schema]

full_good_schema = {
    "id": int,
    "name": str,
    "price": Or(int, float),
    # breaked test with mock in test_api_mock
    "manufacture_date": Or(str, datetime.date),
    "picture_url": str
}

order_schema = {
    "id": int,
    "customer_name": str,
    "delivery_address": str,
    "notes": str,
    # why? couse breaked test with mock in test_api_mock
    "order_date": Or(str, datetime.date),
    "status": str
}
orders_schema = [order_schema]
