'''
Simple RestAPI server with APIFlask, postgresql (psycopg2)
run module, open http://localhost:5000 for Swagger UI
or use Postman
for saving swagger openAPI schema to file use command in terminal.
pwd must be the same as where app.py
flask spec --output openapi.json
'''
import os
from time import sleep
from flask import redirect
from apiflask import APIFlask, abort

import schemas
from routes import configure_routes


app = APIFlask(__name__)
configure_routes(app)
app.url_map.strict_slashes = False  # open /goods/ as /goods
app.config['DESCRIPTION'] = 'RestAPI server with Apiflask and postgresql'
app.config['BASE_RESPONSE_SCHEMA'] = schemas.BaseResponse
# the data key should match the data field name in the base response schema
# defaults to "data"
app.config['BASE_RESPONSE_DATA_KEY '] = 'data'


if __name__ == "__main__":
    # while True:
    app.run(debug=1, host='0.0.0.0')
