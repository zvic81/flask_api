# for test put in console pytest -s -v -m app
# need started postgres! docker compose start postgres
import pytest
import sys
import os.path
from pprint import pprint
from apiflask import APIFlask
import json
app_dir = (os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')) + '/apps/')
sys.path.append(app_dir)
from routes import configure_routes
import schemas
# pprint(sys.path)


@pytest.fixture
def config_apllication():
    app = APIFlask(__name__)
    configure_routes(app)
    client = app.test_client()
    return client


@pytest.mark.app
def test_base_route(config_apllication):
    url = '/'
    response = config_apllication.get(url)
    assert response.status_code == 302  # test redirect to localhost:5000/docs"
    url = '/docs'
    response = config_apllication.get(url)
    assert response.status_code == 200  # test request swagger interface


@pytest.mark.app
def test_get_route(config_apllication):
    url = '/goods'
    response = config_apllication.get(url)
    assert response.status_code == 200


@pytest.mark.app
def test_post_route_success(config_apllication):
    url = '/goods'
    mock_request_data = {'name': 'funta', 'manufacture_date': '2019-02-05',
                         'price': 21, 'picture_url': 'pic.com/mypic.jpg', }
    response = config_apllication.post(url, json=mock_request_data)
    # pprint(response.get_data())
    assert response.status_code == 201, pprint(response.get_data())


# test if server get failure for not correct json
@pytest.mark.app
def test_post_route_failure(config_apllication):
    url = '/goods'
    mock_request_data = {'names': 'funta', 'manufacture_date': '2019-02-05',
                         'price': 21, 'picture_url': 'pic.com/mypic.jpg', }
    response = config_apllication.post(url, json=mock_request_data)
    # pprint(response.get_data())
    assert response.status_code == 400, pprint(response.get_data())
