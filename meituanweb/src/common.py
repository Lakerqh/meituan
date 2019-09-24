from flask import Flask, session,redirect,url_for,request,make_response
from datetime import datetime,timedelta
import mysql.connector
import json

app = Flask(__name__,static_url_path='/static')
class Query:
    def conn(self):
        db = mysql.connector.connect(user='root', password='123456', database='test')
        return db