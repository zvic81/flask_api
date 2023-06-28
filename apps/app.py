'''
Simple RestAPI server with FastAPI, SQLAlchemy
run module, open http://localhost:5000 for Swagger UI
or use Postman
pwd must be the same as where app.py
uvicorn app:app --reload --host 127.0.0.1 --port 5000
'''
from datetime import timedelta
from fastapi import FastAPI
import logging
import logging.config
from log4mongo.handlers import MongoHandler

from routes import router_goods, router_orders, router_auth
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
app.include_router(router_auth)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
