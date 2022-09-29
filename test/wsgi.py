from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hallow wourld!</h1>'

@app.route('/about')
def about():
    return '<h2>testing flask application.</p> vzaharov</h2>'
@app.route('/<string:name>')
def helow(name):
    return f'hellow, {name}'

if __name__ == '__main__':
    app.run()

