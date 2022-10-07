from flask import Flask,jsonify,abort,request
import psycopg2
from config import host,user,password,db_name,index_mes #config for database postgres
# db.py - functions for bd access - select_all_db(connection),select_id_db(connection,id)
#insert_db(connection,good_list),update_id_db(connection,id,good_list),delete_id_db(connection,id),close_db(connection)
import db

app = Flask(__name__)

connection=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
connection.autocommit = True

@app.route('/')
def index():
    return index_mes

@app.route('/goods', methods=['GET'])
def get_goods():
    goods=db.select_all_db(connection)
    return jsonify(goods),200

@app.route('/goods/<int:good_id>', methods=['GET'])
def get_good_id(good_id):
    good=db.select_id_db(connection,good_id)
    if len(good)==0:
        return jsonify({'error':'no id '+str(good_id)}),404
    return jsonify(good),200

@app.route('/goods', methods=['POST'])
def create_good():
    if not request.get_json(silent=True,force=True):
        return jsonify({'error':'no json'}),400
    good=[
        request.json['name'],
        request.json.get('price',""),
        request.json.get('manufacture_date',""),
        request.json.get('picture_url',"")
    ]
    res=db.insert_db(connection,good)
    return jsonify({'append':res[0]}),201

@app.route('/goods/<int:good_id>', methods=['PUT'])
def put_good_id(good_id):
    if not request.get_json(silent=True,force=True):
        return jsonify({'error':'no json'}),400
    good=[
        request.json['name'],
        request.json.get('price',""),
        request.json.get('manufacture_date',""),
        request.json.get('picture_url',"")
    ]
    res=db.update_id_db(connection,good_id,good)
    if not res:
        return jsonify({'error':'no id '+str(good_id)}),404        
    return jsonify({'update':good_id}),200

@app.route('/goods/<int:good_id>', methods=['DELETE'])
def delete_good_id(good_id):
    res=db.delete_id_db(connection,good_id)
    if res[-1]=='0':
        return jsonify({'Error':'no id '+str(good_id)}),404
    return jsonify({'delete ':good_id}),200


if __name__ == "__main__":
    app.run(debug=True)
