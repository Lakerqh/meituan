from flask import Flask, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import config

app = Flask(__name__)
 
app.config.from_object(config)
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)


@app.route('/index')
def index_foo():
    return 'index'

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name',name)
    return response

@app.route('/hello')
def hello():
    return 'setcookie'