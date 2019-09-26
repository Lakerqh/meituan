# -*- coding: utf-8 -*-ENSE for more details.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)

from pyadmin import views, errors