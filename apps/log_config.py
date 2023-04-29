# config for logging, use handler 'mongo' for saving onto mongoDB

config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
       'mongo': {
            'class': 'log4mongo.handlers.MongoHandler',
            'host': 'localhost',
            'port': 27017,
            'database_name': 'mongo_logs',
            'collection': 'logs',
            'level': 'DEBUG',
        },
    },
    'loggers':{
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',

        },
        'simple': {
            'handlers': ['console',],
            'level': 'DEBUG',
        },
        'mongo': {
            'handlers': ['mongo',],
            'level': 'DEBUG',
        }
    }
}
