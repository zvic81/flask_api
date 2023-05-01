import pymongo
from pymongo.errors import ConnectionFailure
from datetime import datetime


def is_mongo_run() -> int:
    client = pymongo.MongoClient()
    try:
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("ERROR, mongoDB not available")
        return 1
    return 0

def select_logs_from_mongo(timestart: datetime, timeend: datetime, module:str = None) -> dict:
    if is_mongo_run():
        return 1
    client = pymongo.MongoClient('localhost', 27017)
    db = client['mongo_logs']
    collection = db['logs']
    query = {"$and" : [
        {'timestamp':{"$gte": timestart}},
        {'timestamp':{"$lte": timeend}}
        ]
    }
    if module and module != 'all':
        query['$and'].append({'module': module})
    res = collection.find(query, {'message':1, '_id':0, 'timestamp':1, 'level':1 , 'module':1})
    return list(res)


if __name__ == "__main__":
    r = select_logs_from_mongo(datetime(2023,4,30, 18,00,00), datetime(2023,5,2, 00,00,00), 'app')
    print(r)
