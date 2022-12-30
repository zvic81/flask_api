#  testing db functions. write in console pytest -s -v -m db
import pytest
from pytest_schema import schema
import sys
import os.path
from pprint import pprint
app_dir = (os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')) + '/apps/')
sys.path.append(app_dir)
import db
from schemas_validation import short_goods_schema, full_good_schema, orders_schema


@pytest.mark.db
def test_select_all_goods_db():
    res = db.select_all_goods_db()
    pprint(res)
    assert res
    assert type(res) == list
    assert schema(short_goods_schema) == res


@pytest.mark.db
def test_select_all_orders_db():
    res = db.select_all_orders_db()
    assert res
    assert type(res) == list
    assert schema(orders_schema) == res


@pytest.mark.db
def test_insert_select_delete_good_db():
    good = {
        "name": "test_name",
        "price": 666,
        "manufacture_date": '2019-02-05',
        "picture_url": "pic.com/mypic.jpg"
    }
    id_good = db.insert_good_db(good)
    assert id_good > 0  # test if items added to db

    db.select_id_good_db(id_good)

    pass