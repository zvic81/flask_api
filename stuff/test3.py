from flask import Flask,jsonify,abort,request
import psycopg2
from config import host,user,password,db_name #config for database postgres
import db # functions for bd access -select_all_db(connection) 

app = Flask(__name__)

connection=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
connection.autocommit = True

goods=[]


@app.route('/goods', methods=['GET'])
def get_goods():
    #goods=select_all_db(connection)
    return jsonify({'goods':goods})

@app.route('/goods/<int:good_id>', methods=['GET'])
def get_good_id(good_id):
    #good=select_id_db(connection,good_id):
    if len(good)==0:
        abort(404)
    return jsonify({'good': good[0]})

@app.route('/goods', methods=['POST'])
def create_good():
    if not request.json:# or not 'name' in request.json:
        abort(400)
    good={
        'id' : goods[-1]['id']+1,
        'name' : request.json['name'],
        'price' : request.json.get('price',""),
        'manufacture_date' : request.json.get('request.json',""),
        'picture_url' : request.json.get('picture_url',"")
    }
    goods.append(good)
    return jsonify({'good':good}),201

@app.route('/goods/<int:good_id>', methods=['PUT'])
def put_good_id(good_id):
    good=list(filter(lambda t: t['id'] == good_id,goods))
    if len(good)==0:
        abort(404)
    good[0]['name']=request.json.get('name',"")
    good[0]['price']=request.json.get('price',"")
    good[0]['manufacture_date']=request.json.get('manufacture_date',"")
    good[0]['picture_url']=request.json.get('picture_url',"")
    return jsonify({'good': good[0]})

@app.route('/goods/<int:good_id>', methods=['DELETE'])
def delete_good_id(good_id):
    good=list(filter(lambda t: t['id'] == good_id,goods))
    if len(good)==0:
        abort(404)
    goods.remove(good[0])
    return jsonify({'result':True})


if __name__ == "__main__":
    #app.run(debug=True)
    print ('test')
    goods=db.select_all_db(connection)
    print (goods)
    print ('*'*50)
 #   print ("insert ",db.insert_db(connection,('hepe',112,'05/07/22','pic112')))
#    goods=db.select_all_db(connection)
#    print (goods)
    print (db.update_id_db(connection,3,('keyboard666',666,'05/07/22','pic112')))
#    print (db.delete_id_db(connection,4))
    print (db.select_all_db(connection))



    db.close_db(connection)


    
