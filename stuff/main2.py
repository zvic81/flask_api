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
def get_goods2(good_id):
    good=list(filter(lambda t: t['id'] == good_id,goods))
    print (good)
    if len(good)==0:
        abort(404)
    return jsonify({'good': good[0]})

@app.route('/goods', methods=['POST'])
def create_good():
    if not request.json:# or not 'name' in request.json:
        abort(400)
    print (request.json.get('name'))
        
   # good={
    #    'id' : goods[-1]['id']+1,
     #   'name' : request.json['name'],
      #  'price' : request.json.get('price',"")
    #}
    #goods.append(good)
    return jsonify({'good':goods}),201


if __name__ == "__main__":
    app.run(debug=True)
