from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'October 13 1986'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' +  name + '!'

@app.route('/add/<int:firstparam>/<int:secondparam>')
def add(firstparam, secondparam):
    result = firstparam + secondparam
    return str(result)

@app.route('/multiply/<int:firstparam>/<int:secondparam>')
def multiply(firstparam, secondparam):
    result = firstparam * secondparam
    return str(result)
    
@app.route('/substruct/<int:firstparam>/<int:secondparam>')
def sustruct(firstparam, secondparam):
    result = firstparam / secondparam
    return str(result)

@app.route('/favoritefoods')
def favoritefoods():
    favorite_foods = ['sandwich', 'smoked ham', 'cookie', 'chocolate']
    return jsonify(favorite_foods)