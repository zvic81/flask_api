'''
Simple RestAPI server with APIFlask, postgresql (psycopg2)
run module, open http://localhost:5000 for Swagger UI
or use Postman
for saving swagger openAPI schema to file use command in terminal.
pwd must be the same as where app.py
flask spec --output openapi.json
uvicorn main:app --reload
'''
from datetime import timedelta
from fastapi import FastAPI
import logging
import logging.config
from log4mongo.handlers import MongoHandler
from routes import router_goods, router_orders
import log_config
from mongo_functions import is_mongo_run

if not is_mongo_run():
    logging.config.dictConfig(log_config.config_mongo)
else:
    logging.config.dictConfig(log_config.config_console)
logger = logging.getLogger('my_log')
logger.info("app started!!!")

app = FastAPI()
app.include_router(router_goods)
app.include_router(router_orders)
