'''
Simple RestAPI server with APIFlask, postgresql (psycopg2)
run module, open http://localhost:5000 for Swagger UI
or use Postman
for saving swagger openAPI schema to file use command in terminal.
pwd must be the same as where app.py
flask spec --output openapi.json
'''
from datetime import timedelta
from apiflask import APIFlask
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
app.config["JWT_SECRET_KEY"] = "mysecretkey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.secret_key = 'BAD_SECRET_KEY'


if __name__ == "__main__":
    app.run(debug=0, host='0.0.0.0')
    pass
