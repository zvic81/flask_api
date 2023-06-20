from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from pip._vendor import cachecontrol
import google.auth.transport.requests
from google.oauth2 import id_token
# from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import redis
import json
import time
import logging

import db
from schema import GoodIn, OrderIn
import oauth_functions
import mongo_functions

# jwt = JWTManager()
logger = logging.getLogger('my_log')
router_goods = APIRouter(prefix="/api/v1", tags=["goods"],)
router_orders = APIRouter(prefix="/api/v1", tags=["orders"],)


@router_goods.get("/")
def index():
    return RedirectResponse("/docs")


@router_goods.get("/goods")
def get_goods():
    goods = db.select_all_goods_db()
    logger.info("return get('/goods')")
    return {
        'data': goods,
        'code': 200,
    }


@router_orders.get("/orders")
def get_orders():
    orders = db.select_all_orders_db("mihrin@gmail.com")
    logger.info(f"return get('/orders') for user ")
    return {
        'data': orders,
        'code': 200,
    }


@router_goods.get("/goods/{good_id}")
def get_good_id(good_id: int):
    good = db.select_id_good_db(good_id)
    logger.info(f"return get goods for id={good_id}")
    return {
        'data': good,
        'code': 200,
    }


@router_goods.post("/goods")
def create_good(good: GoodIn):
    res = {'id': db.insert_good_db(good.dict())}
    try:
        with redis.Redis() as r:
            r.flushdb()
    except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
        logger.info("ERROR get_goods_cached(): redis not ready!")
    logger.info(f"post goods for {res}")
    return {
        'data': res,
        'code': 201,
    }


@router_orders.post("/orders")
def create_order(order: OrderIn):
    res = {'id': db.insert_order_db(order.dict())}
    logger.info(f"post orders for {res}")
    return {
        'data': res,
        'code': 201,
    }

@router_goods.put("/goods/{good_id}")
def put_good_id(good_id: int, good: GoodIn):
    res = {'id': db.update_id_good_db(good_id, good.dict())}
    try:
        with redis.Redis() as r:
            r.flushdb()
    except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
        print("ERROR get_goods_cached(): redis not ready!")
    logger.info(f"put goods for {res}")
    return {
        'data': res,
        'code': 200,
    }

@router_goods.delete("/goods/{good_id}")
def delete_good_id(good_id):
    res = db.delete_id_good_db(good_id)
    if res == -1:
        raise HTTPException(status_code=404, detail="Error_no_id")
    logger.info(f"delete goods for id={good_id}")
    return {
        'data': res,
        'code': 204,
    }

'''
def configure_routes(app):
    jwt.init_app(app)


    @app.get('/login')
    def login():
        authorization_url, state = oauth_functions.flow.authorization_url()
        return redirect(authorization_url, code=302)

    @app.get("/callback")
    def callback():
        oauth_functions.flow.fetch_token(authorization_response=request.url)
        credentials = oauth_functions.flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(
            session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=oauth_functions.GOOGLE_CLIENT_ID
        )
        email = id_info.get("email")
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        logger.info(f"jwt token return succesfully for {email}")
        return jsonify(access_token=access_token, refresh_token=refresh_token)

    @app.get("/refresh_token")
    @jwt_required(refresh=True)
    def refresh():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        logger.info(f'return new token in refresh for {identity}')
        return jsonify(access_token=access_token)

    @app.get("/goods_cached")
    @app.output(schemas.GoodsOutCached(many=True), status_code=200)
    def get_goods_cached():
        output_redis = None
        goods_cached = []
        try:
            with redis.Redis() as r:
                output_redis = r.get('goods')
        except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
            logger.info("ERROR get_goods_cached(): redis not ready!")

        if output_redis:
            goods_cached = json.loads(output_redis)
        else:
            tmp = db.select_all_goods_db()
            for i in tmp:
                goods_cached.append(
                    {'id': i[0], 'name': i[1], 'price': len(i[1]) + 0.99})
                time.sleep(0.9)
            try:
                with redis.Redis() as r:
                    r.set('goods', json.dumps(goods_cached))
            except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
                logger.info("ERROR get_goods_cached(): redis not ready!")
        logger.info("return goods_cached ")
        return {
            'data': goods_cached,
            'code': 200,
        }

    @app.get("/logs")
    @app.input(schemas.LogsFilterIn, location='query')
    @app.output(schemas.LogsOut(many=True), status_code=200)
    def get_logs(query):
        result = (mongo_functions.select_logs_from_mongo(query['timestart'],
                                                         query['timeend'], query.get('module')))
        if result == 1:
            logger.info(f"Error get logs, server Mongo not ready")
            abort(404, 'Error_Mongo_not_ready')
        logger.info(f"return logs from Mongo")
        return {
            'data': result,
            'code': 200,
        }

'''
