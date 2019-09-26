# -*- coding: utf-8 -*-
from flask import flash

from pyadmin import app, db
from pyadmin.models import Message


@app.route('/', methods=['GET'])
def index():
    return '12'