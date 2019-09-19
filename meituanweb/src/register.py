#coding=utf-8
from common import *

query = Query()
db = query.conn()

@app.route('/register', methods=['GET', 'POST'])
def sys_register():
    cursor = db.cursor()
    username = request.args.get('username')
    password = request.args.get('password')
    print('22222',username,password)
    sql = "INSERT INTO users(id, username, password) VALUE('%s','%s','%s')" % (4,'LLL','12')
    try:
        if request.method == 'GET':
            print('11111111111111')
            cursor.execute(sql)
            db.commit()
            return 'ok'
    except Exception as e:
        return e
    db.close()