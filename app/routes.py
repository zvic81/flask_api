
from apiflask import APIFlask, abort
from flask import redirect
from time import sleep
import os
import db
import schemas


def configure_routes(app):

    @app.get('/')
    @app.doc(hide=True)
    def index():
        data = {'message': 'Hello!'}
        # open swagger index page
        return redirect("http://localhost:5000/docs", code=302)

    @app.get('/goods')
    @app.output(schemas.GoodsOut(many=True))
    def get_goods():
        goods = db.select_all_goods_db()
        return {
            'data': goods,
            'code': 200,
        }

    @app.get('/orders')
    @app.output(schemas.OrdersOut(many=True))
    def get_orders():
        orders = db.select_all_orders_db()
        return {
            'data': orders,
            'code': 200,
        }

    @app.get('/goods/<int:good_id>')
    @app.output(schemas.GoodOut)
    def get_good_id(good_id):
        good = db.select_id_good_db(good_id)
        if len(good) == 0:
            abort(404, 'Error:no id')
        return {
            'data': good[0],
            'code': 200,
        }

    @app.post('/goods')
    @app.input(schemas.GoodIn)
    @app.output(schemas.MessageOk, status_code=201)
    def create_good(data):
        if not data:
            return abort(400, 'Error:no json')
        good = [
            data['name'],
            data['price'],
            data['manufacture_date'],
            data['picture_url']
        ]
        res = {'id': db.insert_good_db(data)}
        return {
            'data': res,
            'code': 201,
        }

    @ app.post('/orders')
    @ app.input(schemas.OrderIn)
    @ app.output(schemas.MessageOk, status_code=201)
    def create_order(data):
        if not data:
            return abort(400, 'Error:no json')
        res = {'id': db.insert_order_db(data)}
        return {
            'data': res,
            'code': 201,
        }

    @ app.put('/goods/<int:good_id>')
    @ app.input(schemas.GoodIn)
    @ app.output(schemas.MessageOk, status_code=201)
    def put_good_id(good_id, data):
        if not data:
            return abort(400, 'Error:no json')
        res = {'id': db.update_id_good_db(good_id, data)}
        if not res:
            return abort(404, 'Error:no id')
        return {
            'data': res,
            'code': 200,
        }

    @ app.delete('/goods/<int:good_id>')
    @ app.output(schemas.MessageOk, status_code=204)
    def delete_good_id(good_id):
        res = db.delete_id_good_db(good_id)
        if res[-1] == '0':
            return abort(404, 'Error:no id')
        return {
            'data': {'1': 1},
            'code': 200,
        }
