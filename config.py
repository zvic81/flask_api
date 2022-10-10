#from config import host,user,password,db_name
host = "192.168.0.103"
user = "flask_user"
password = "flask_user"
db_name = "flask_db"

index_mes=''' Use GET <a href=http://127.0.0.1:5000/goods>http://127.0.0.1:5000/goods</a> for all goods<p>
    GET <i>http://127.0.0.1:5000/goods/3</i> for goods id=3<p>
    POST <i>http://127.0.0.1:5000/goods</i> for append goods with json<p>
    PUT <i>http://127.0.0.1:5000/goods/3</i> for change goods id=3 with json<p>
    DELETE <i>http://127.0.0.1:5000/goods/3</i> for delete goods id=3<p>
    format json:
    {
    "name":"bananas",
    "price":8,
    "manufacture_date":"2/11/11",
    "picture_url":"gogle.com"
    }
    '''
