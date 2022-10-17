from flask import Flask, jsonify, abort, request, redirect #render_template
import psycopg2

import os
from flask.views import MethodView
from flasgger import Swagger
from config import host, user, password, db_name  # config for database postgres
# db.py - functions for bd access - select_all_db(connection),select_id_db(connection,id)
# insert_db(connection,good_list),update_id_db(connection,id,good_list),delete_id_db(connection,id),close_db(connection)
import db

app = Flask(__name__)
app.url_map.strict_slashes = False #open /goods/ as /goods

app.config['SWAGGER'] = {
    'title': 'Flasgger Parsed Method/Function View Example',
    'doc_dir': './templates'
}
swag = Swagger(
    app,
    template_file=os.path.join(
        os.getcwd(), 'templates', 'openapi.yml'),
    parse=True)

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
connection.autocommit = True


@app.route('/')
def index():
    return redirect("http://localhost:5000/apidocs",code=302) #open swagger index page
    # return render_template('index.html', name='vzaharov')


@app.route('/goods', methods=['GET'])
def get_goods():
    goods = db.select_all_db(connection)
    return jsonify(goods), 200


@app.route('/goods/<int:good_id>', methods=['GET'])
def get_good_id(good_id):
    good = db.select_id_db(connection, good_id)
    if len(good) == 0:
        return jsonify({'error': 'no id '+str(good_id)}), 404
    return jsonify(good), 200


@app.route('/goods', methods=['POST'])
def create_good():
    if not request.get_json(silent=True, force=True):
        return jsonify({'error': 'no json'}), 400
    good = [
        request.json['name'],
        request.json.get('price', ""),
        request.json.get('manufacture_date', ""),
        request.json.get('picture_url', "")
    ]
    res = db.insert_db(connection, good)
    return jsonify({'id': res[0]}), 201


@app.route('/goods/<int:good_id>', methods=['PUT'])
def put_good_id(good_id):
    if not request.get_json(silent=True, force=True):
        return jsonify({'error': 'no json'}), 400
    good = [
        request.json['name'],
        request.json.get('price', ""),
        request.json.get('manufacture_date', ""),
        request.json.get('picture_url', "")
    ]
    res = db.update_id_db(connection, good_id, good)
    if not res:
        return jsonify({'error': 'no id '+str(good_id)}), 404
    return '', 200


@app.route('/goods/<int:good_id>', methods=['DELETE'])
def delete_good_id(good_id):
    res = db.delete_id_db(connection, good_id)
    if res[-1] == '0':
        return jsonify({'error': 'no id '+str(good_id)}), 404
    return '', 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
