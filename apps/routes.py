from flask import redirect, abort,jsonify, request
import requests
from pip._vendor import cachecontrol
import google.auth.transport.requests
from google.oauth2 import id_token
from flask_jwt_extended import JWTManager,create_access_token, create_refresh_token,jwt_required,get_jwt_identity
import db
import schemas
import oauth_functions



jwt = JWTManager()

def configure_routes(app):
    jwt.init_app(app)

    @app.get('/')
    @app.doc(hide=True)
    def index():
        data = {'message': 'Hello!'}
        # open swagger index page
        return redirect("/docs", code=302)

    @app.get('/goods')
    @app.output(schemas.GoodsOut(many=True), status_code=200)
    def get_goods():
        goods = db.select_all_goods_db()
        return {
            'data': goods,
            'code': 200,
        }

    @app.get('/orders')
    @jwt_required()
    @app.output(schemas.OrdersOut(many=True), status_code=200)
    def get_orders():
        current_user = get_jwt_identity()
        print(current_user)

        orders = db.select_all_orders_db(current_user)
        return {
            'data': orders,
            'code': 200,
        }

    @app.get('/goods/<int:good_id>')
    @app.output(schemas.GoodOut, status_code=200)
    def get_good_id(good_id):
        good = db.select_id_good_db(good_id)
        if len(good) == 0:
            abort(404, 'Error:no id')
        return {
            'data': good,
            'code': 200,
        }

    @app.post('/goods')
    @app.input(schemas.GoodIn)
    @app.output(schemas.MessageOk, status_code=201)
    def create_good(data):
        if not data:
            return abort(400, 'Error:no json')
        res = {'id': db.insert_good_db(data)}
        return {
            'data': res,
            'code': 201,
        }

    @app.post('/orders')
    @app.input(schemas.OrderIn)
    @app.output(schemas.MessageOk, status_code=201)
    def create_order(data):
        if not data:
            return abort(400, 'Error:no json')
        res = {'id': db.insert_order_db(data)}
        return {
            'data': res,
            'code': 201,
        }

    @app.put('/goods/<int:good_id>')
    @app.input(schemas.GoodIn)
    @app.output(schemas.MessageOk, status_code=201)
    def put_good_id(good_id, data):
        if not data:
            return abort(400, 'Error:no json')
        res = {'id': db.update_id_good_db(good_id, data)}
        if not res:
            return abort(404, 'Error:no id')
        return {
            'data': res,
            'code': 201,
        }

    @app.delete('/goods/<int:good_id>')
    @app.output(schemas.MessageOk, status_code=204)  # if status 204 - no json
    def delete_good_id(good_id):
        res = db.delete_id_good_db(good_id)
        if res[-1] == '0':
            return abort(404, 'Error:no id')
        return {
            'data': 1,  # dont work because  MessageOk(Schema) forbid
            'code': 204,
        }
    
    @app.get('/login')
    def login():
        authorization_url, state = oauth_functions.flow.authorization_url()
        return redirect(authorization_url,code=302)
    
    @app.get("/callback")
    def callback():
        oauth_functions.flow.fetch_token(authorization_response=request.url)
        credentials = oauth_functions.flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=oauth_functions.GOOGLE_CLIENT_ID
        )
        print(f' ******************id_info=   {id_info}')
        email = id_info.get("email")
        print(f'logged email = {email}')
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return jsonify(access_token=access_token, refresh_token=refresh_token)


    @app.get("/refresh")
    @jwt_required(refresh=True)
    def refresh():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        print('return new token in refresh')
        return jsonify(access_token=access_token)
 
    
   