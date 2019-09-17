#coding=utf-8
from common import *

query = Query()
db = query.conn()

@app.route('/')
def first():
    return app.send_static_file('index.html')

@app.route('/fields')
def index_fields():
    cursor = db.cursor()
    sql = 'select * from users'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        keyName = ['id','username','password']
        arr = []
        for row in results:
            arr.append(dict(zip(keyName,row)))

        data = {
            'data': arr
        }
        return data
    except Exception as e:  
        return e
    db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234)