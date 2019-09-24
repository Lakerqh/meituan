# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    message = db.Column(db.Text)

@app.route('/add',methods = ['POST'])
def add_note():
    name = request.form['name']
    message = request.form['message']
    note1 = Note(name=name,message=message)
    db.session.add(note1)
    db.session.commit()
    db.session.close()  
    
    data = {
        'code':200,
        'msg':'添加成功'
    }
    return data

@app.route('/deletenote',methods=['POST'])
def delete_note():
    id = request.form['id']
    results = Note.query.filter_by(id=id).first()
    db.session.delete(results)
    db.session.commit()
    db.session.close()
    data = {
        'code':200,
        'msg':'删除成功'
    }
    return data

@app.route('/updatenote',methods=['POST'])
def update_note():
    id = request.form['id']
    name = request.form['name']
    message = request.form['message']

    results = Note.query.filter_by(id=id).first()
    results.name = name
    results.message = message
    db.session.commit()
    db.session.close()
    data = {
        'code':200,
        'msg':'修改成功'
    }
    return data

@app.route('/list',methods=['GET'])
def get_list():
    result = Note.query.all()
    resData = []
    for x in result:
        resData.append({
            'id':x.id,
            'name':x.name,
            'message':x.message
        })
    data = {
        'code':200,
        'result':resData
    }
    return data
    

