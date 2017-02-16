from flask import Flask, render_template

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
    sub = firstparam + secondparam
    return str(sub)