# coding=utf-8
from common import *

query = Query()
db = query.conn()


@app.route('/')
def first():
    return app.send_static_file('index.html')


@app.route('/fields')
def index_fields():
    cursor = db.cursor()
    sql = 'select * from t_fields'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        keyName = ['id', 'goods_name']
        arr = []
        for row in results:
            arr.append(dict(zip(keyName, row)))

        data = {
            'data': arr
        }
        return data
    except Exception as e:
        return e
    db.close()


@app.route('/sub_field', methods=['GET', 'POST'])
def sub_field():
    cursor = db.cursor()
    fid = request.args.get('fid')
    print(fid)
    sql = 'select * from t_sub_fields where field_id = 1 order by id asc'
    try:
        if request.method == 'GET':
            cursor.execute(sql)
            results = cursor.fetchall()
            data = {
                'data':results
            }
            return data
    except Exception as e:
        return e
    db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
