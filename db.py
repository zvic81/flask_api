
def ConnectDB(connection,host,user,password,db_name):
    connection=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
    connection.autocommit = True
   
def SelectDB(connection):
    with connection.cursor() as g:
        g.execute("SELECT * FROM goods;")
        cnt=g.fetchall()
        return cnt
        #for row in cnt:
         #   print (row)
def CloseDB(connection):
    if connection:
        connection.close()
        print("<connection closed>")
    
         
    
