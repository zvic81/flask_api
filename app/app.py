'''
Simple RestAPI server with APIFlask, postgresql (psycopg2)
run module, open http://localhost:5000 for Swagger UI
or use Postman
for saving swagger openAPI schema to file use command in terminal.
pwd must be the same as where app.py
flask spec --output openapi.json
'''
import os
from flask import redirect
from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String, Field, Date
import psycopg2
# db.py - functions for bd access - select_all_db(connection),select_id_db(connection,id)
# insert_db(connection,good_list),update_id_db(connection,id,good_list),delete_id_db(connection,id),close_db(connection)
import db
# config for database postgres
from config import host, user, password, db_name, port


class BaseResponse(Schema):
    data = Field()  # the data key
    # message = String()
    code = Integer()


class GoodsOut(Schema):  # list of short goods for response
    id = Integer(metadata={'example': 2})
    name = String(metadata={'example': 'Coffee'})


class GoodIn(Schema):  # one good with full fields
    name = String(required=True, metadata={'example': 'Coffee'})
    price = Integer(metadata={'example': 21})
    manufacture_date = String(metadata={'example': '02/08/2019'})
    picture_url = String(metadata={'example': 'pic.com/mypic.jpg'})


class GoodOut(GoodIn):  # one good with full fields
    id = Integer()


class OrdersOut(Schema):    # list of orders for responce
    id = Integer()
    order_date = Date()
    customer_name = String()
    customer_email = String()
    delivery_address = String()
    status = String()
    notes = String()


class MessageOk(Schema):
    id = Integer()


app = APIFlask(__name__)
app.url_map.strict_slashes = False  # open /goods/ as /goods
app.config['DESCRIPTION'] = 'RestAPI server with Apiflask and postgresql'

app.config['BASE_RESPONSE_SCHEMA'] = BaseResponse
# the data key should match the data field name in the base response schema
# defaults to "data"
app.config['BASE_RESPONSE_DATA_KEY '] = 'data'


connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    port=port
)
connection.autocommit = True


@app.get('/')
@app.doc(hide=True)
def index():
    data = {'message': 'Hello!'}
    # open swagger index page
    return redirect("http://localhost:5000/docs", code=302)


@app.get('/goods')
@app.output(GoodsOut(many=True))
def get_goods():
    goods = db.select_all_db(connection)
    return {
        'data': goods,
        'code': 200,
    }


@app.get('/orders')
@app.output(OrdersOut(many=True))
def get_orders():
    orders = db.select_all_orders_db(connection)
    print(orders)
    return {
        'data': orders,
        'code': 200,
    }


@app.get('/goods/<int:good_id>')
@app.output(GoodOut)
def get_good_id(good_id):
    good = db.select_id_db(connection, good_id)
    if len(good) == 0:
        abort(404, 'Error:no id')
    return {
        'data': good[0],
        'code': 200,
    }


@app.post('/goods')
@app.input(GoodIn)
@app.output(MessageOk, status_code=201)
def create_good(data):
    if not data:
        return abort(400, 'Error:no json')
    good = [
        data['name'],
        data['price'],
        data['manufacture_date'],
        data['picture_url']
    ]
    res = {'id': db.insert_db(connection, good)[0]}
    return {
        'data': res,
        'code': 201,
    }


@app.put('/goods/<int:good_id>')
@app.input(GoodIn)
@app.output(MessageOk, status_code=201)
def put_good_id(good_id, data):
    if not data:
        return abort(400, 'Error:no json')
    good = [
        data['name'],
        data['price'],
        data['manufacture_date'],
        data['picture_url']
    ]
    res = {'id': db.update_id_db(connection, good_id, good)}
    if not res:
        return abort(404, 'Error:no id')
    return {
        'data': res,
        'code': 200,
    }


@app.delete('/goods/<int:good_id>')
@app.output(MessageOk, status_code=204)
def delete_good_id(good_id):
    res = db.delete_id_db(connection, good_id)
    if res[-1] == '0':
        return abort(404, 'Error:no id')
    return {
        'data': {'1': 1},
        'code': 200,
    }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
