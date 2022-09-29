from config import host,user,password,db_name
import db

print ('test db')
db.ConnectDB(host,user,password,db_name)
res=db.SelectDB()
for i in res:
    print (i)
db.CloseDB()

