# testing with pytest and MOCKING for imitate db function. DONT need started postgres!
# for test put in console *** pytest -s -v -m app_mock ***

import pytest
from pytest_schema import schema
import datetime
import sys
import os.path
from pprint import pprint
from apiflask import APIFlask
# import json
app_dir = (os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')) + '/apps/')
sys.path.append(app_dir)
import routes
import db
import schemas
from schemas_validation import short_goods_schema, full_good_schema, orders_schema


@pytest.fixture
def config_apllication():
    app = APIFlask(__name__)
    routes.configure_routes(app)
    app.url_map.strict_slashes = False  # open /goods/ as /goods
    app.config['DESCRIPTION'] = 'RestAPI server with Apiflask and postgresql'
    app.config['BASE_RESPONSE_SCHEMA'] = schemas.BaseResponse
    app.config['BASE_RESPONSE_DATA_KEY '] = 'data'
    client = app.test_client()
    return client


@pytest.mark.app_mock
def test_base_route(config_apllication):
    url = '/'
    response = config_apllication.get(url)
    assert response.status_code == 302  # test redirect to localhost:5000/docs"
    url = '/docs'
    response = config_apllication.get(url)
    assert response.status_code == 200  # test request swagger interface


@pytest.mark.app_mock
def test_get_all_goods_route(config_apllication, mocker):
    mocker.patch('db.select_all_goods_db', return_value=[{
                 'id': 13, 'name': "name14"}, {
        'id': 15, 'name': "name16"}])
    url = '/goods'
    response = config_apllication.get(url)
    assert response.status_code == 200
    p = response.get_json()
    # pprint(p)
    assert p['code'] == 200
    assert p['data'] == schema(short_goods_schema)
    assert p['data'][0] == {'id': 13, 'name': "name14"}


@pytest.mark.app_mock
def test_get_all_orders_route(config_apllication, mocker):
    mocker.patch('db.select_all_orders_db', return_value=[{
        'id': 13,
        'order_date': datetime.date(2019, 2, 5),
        'customer_name': 'name13',
        'customer_email': 'email13@l.com',
        'delivery_address': 'Frisco13',
        'status': 'good13',
        'notes': 'notes13',
    }, ])
    url = '/orders'
    response = config_apllication.get(url)
    assert response.status_code == 200
    p = response.get_json()
    assert p['code'] == 200
    assert p['data'] == schema(orders_schema)
    assert p['data'][0]['id'] == 13
    assert p['data'][0]['customer_name'] == 'name13'
    assert p['data'][0]['delivery_address'] == 'Frisco13'


@pytest.mark.app_mock
def test_get_id_good_route(config_apllication, mocker):
    mocker.patch('db.select_id_good_db', return_value={
                 'id': 13, 'name': "name14", 'price': 15,
                 'manufacture_date': datetime.date(2019, 2, 5),
                 'picture_url': "mypic13.com/pic13"})
    url = '/goods/13'
    response = config_apllication.get(url)
    assert response.status_code == 200
    p = response.get_json()
    # pprint(p)
    assert p['code'] == 200
    assert p['data'] == schema(full_good_schema)
    assert p['data'] == {'id': 13, 'name': "name14", 'price': 15,
                         'manufacture_date': '2019-02-05',
                         'picture_url': "mypic13.com/pic13"}


@pytest.mark.app_mock
def test_post_good_route(config_apllication, mocker):
    mocker.patch('db.insert_good_db', return_value=1)
    url = '/goods'
    mock_request_data = {'name': 'funtass', 'manufacture_date': '2019-02-05',
                         'price': 21, 'picture_url': 'pic.com/mypic.jpg', }
    response = config_apllication.post(url, json=mock_request_data)
    assert response.status_code == 201
    p = response.get_json()
    assert p['code'] == 201
    assert p['data'] == {'id': 1}


@pytest.mark.app_mock
def test_post_order_route(config_apllication, mocker):
    mocker.patch('db.insert_order_db', return_value=1)
    url = '/orders'
    mock_request_data = {
        'order_date': '2022-11-05', 'customer_name': 'Carlson',
        'customer_email': 'carlson@gmail.com', 'delivery_address': 'Apatity',
        'notes': 'poor customer',
        'good_item': [{'good_id': 1, 'ammount': 13}]
    }
    response = config_apllication.post(url, json=mock_request_data)
    assert response.status_code == 201
    p = response.get_json()
    assert p['code'] == 201
    assert p['data'] == {'id': 1}


@pytest.mark.app_mock
def test_put_id_good_route(config_apllication, mocker):
    mocker.patch('db.update_id_good_db', return_value=1)
    url = '/goods/13'
    mock_request_data = {'name': 'funtass', 'manufacture_date': '2019-02-05',
                         'price': 21, 'picture_url': 'pic.com/mypic.jpg', }
    response = config_apllication.put(url, json=mock_request_data)
    p = response.get_json()
    assert response.status_code == 201
    assert p['code'] == 201
    assert p['data'] == {'id': 1}


@pytest.mark.app_mock
def test_delete_id_good_route(config_apllication, mocker):
    mocker.patch('db.delete_id_good_db', return_value='DELETE 1')
    url = '/goods/13'
    response = config_apllication.delete(url)
    assert response.status_code == 204  # check delete from BD run correct
    mocker.patch('db.delete_id_good_db', return_value='DELETE 0')
    response = config_apllication.delete(url)
    assert response.status_code == 404  # check delete from BD wrong
