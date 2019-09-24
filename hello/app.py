from flask import Flask,abort,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'jajaj'

@app.route('/hello')
def hello_text():
    return redirect(url_for('helloworld'))

@app.route('/helloworld')
def h_world():
    return 'helloworld'


