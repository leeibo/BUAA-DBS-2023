from flask import Blueprint
from Model import *

delete = Blueprint('delete', __name__)


@delete.route('/api/v1/<table_name>/<id>', methods=['DELETE'])
def delete1_record(table_name, id: str):
    # datas = request.json
    # 根据表名获取对应的 ORM 模型
    model = globals()[table_name]
    # 根据 ID 查询要删除的记录
    record = None
    if table_name == 'departments':
        record = model.query.filter_by(dept_no=id).first()
    elif table_name == 'employees':
        record = model.query.filter_by(emp_no=int(id)).first()
    if not record:
        return jsonify({'error': 'Record not found.'}), 404

    # 删除记录
    try:
        db.session.delete(record)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

    return jsonify({'message': f'{id} row delete into {table_name} successfully'}), 201


# 定义处理 DELETE 请求的路由
# 有两个id
@delete.route('/api/v1/<table_name>/<id1>/<id2>', methods=['DELETE'])
def delete2_record(table_name, id1: int, id2: str):
    # datas = request.json
    # 根据表名获取对应的 ORM 模型
    model = globals()[table_name]
    # 根据 ID 查询要删除的记录
    record = None
    if table_name == 'dept_manager':
        record = model.query.filter_by(emp_no=id1, dept_no=id2).first()
    elif table_name == 'dept_emp':
        record = model.query.filter_by(emp_no=id1, dept_no=id2).first()
    if not record:
        return jsonify({'error': 'Record not found.'}), 404

    # 删除记录
    try:
        db.session.delete(record)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

    return jsonify({'message': f'{id} row delete into {table_name} successfully'}), 201


# 定义处理 DELETE 请求的路由
# 三个id
@delete.route('/api/v1/<table_name>/<id1>/<id2>/<id3>', methods=['DELETE'])
def delete3_record(table_name, id1: int, id2: str, id3: str):
    # datas = request.json
    # 根据表名获取对应的 ORM 模型
    model = globals()[table_name]
    # 根据 ID 查询要删除的记录
    record = None

    if table_name == 'titles':
        record = model.query.filter_by(emp_no=id1, title=id2, from_date=id3).first()
    if not record:
        return jsonify({'error': 'Record not found.'}), 404
    # 删除记录
    try:
        db.session.delete(record)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

    return jsonify({'message': f'{id} row delete into {table_name} successfully'}), 201
