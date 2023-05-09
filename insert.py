from flask import Blueprint
from Model import *

insert = Blueprint('insert', __name__)


@insert.route('/api/v1/<table_name>', methods=['POST'])
def insert_data(table_name):
    data = request.json
    # print(data)
    rows = data['rows']
    Model = globals()[table_name]
    with app.app_context():
        # 根据表格名称创建模型对象
        # 创建模型对象并插入数据
        for o in rows:
            obj = Model(**o)
            db.session.add(obj)
        db.session.commit()
    return jsonify({'message': f'{len(rows)} rows inserted into {table_name} successfully'}), 201
