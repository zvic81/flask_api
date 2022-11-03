from flask import Flask,jsonify,abort,request

app = Flask(__name__)

goods=[
    {
        'id' : 1,
        'name' : 'goods1',
        'price' : 125,
        'manufacture_date' : '10/01/22',
        'picture_url' : 'pic.com/pic11'
    },
    {
        'id' : 2,
        'name' : 'goods2',
        'price' : 985,
        'manufacture_date' : '02/07/22',
        'picture_url' : 'pic.com/pic122'
    }
]

@app.route('/goods', methods=['GET'])
def get_goods():
    return jsonify({'goods':goods})

@app.route('/goods/<int:good_id>', methods=['GET'])
def get_good_id(good_id):
   # def get_task(task_id):
   # for task in tasks:
    #    if t['id'] == tasks_id:
    #        return jsonify({'task': task})
   # abort(404)
    good=list(filter(lambda t: t['id'] == good_id,goods))
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
    app.run(debug=True)
