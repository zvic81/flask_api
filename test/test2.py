import psycopg2
from config import host,user,password,db_name
import db


connection=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
connection.autocommit = True
 
print ('test db')
res=db.SelectDB(connection)
for i in res:
    print (i)
db.CloseDB(connection)

