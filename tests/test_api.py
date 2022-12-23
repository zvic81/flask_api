from pprint import pprint
from apiflask import APIFlask
import json
import sys
import os.path
# sys.path.append(os.path.abspath(os.path.join(
#     os.path.dirname(__file__), os.path.pardir)))
sys.path.append("..")
pprint(sys.path)
# from app import routes
import sys
import os
import app

def test_base_route():
    app = APIFlask(__name__)

    # configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    # assert response.get_data() == b'Hello, World!'
    # assert response.status_code == 200
    # pass
