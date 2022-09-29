import psycopg2
from config import host,user,password,db_name
connection=None

def ConnectDB(host,user,password,db_name):
try:
    global connection=psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    global connection.autocommit = True
    #print(connection.get_dsn_parameters(), "\n")
    #with connection.cursor() as g:
      #  g.execute("SELECT * FROM goods;")
      #  cnt=g.fetchall()
       # for row in cnt:
       #     print (row)
except Exception as _ex:
    print("error with postgreSQL", _ex)

#finally:
 #   if connection:
  #      #cursor.close()
   #     connection.close()
    #    print("<connection closed>")
    
def SelectDB():
    with global connection.cursor() as g:
        g.execute("SELECT * FROM goods;")
        cnt=g.fetchall()
        return cnt
        #for row in cnt:
         #   print (row)
def CloseDB():
    if connection:
        connection.close()
        print("<connection closed>")
    
         
    
