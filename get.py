from flask import Blueprint
from Model import *

get = Blueprint('get', __name__)


def filter_by_attr(table_name, attr, value):
    # 获取 Model 对象的查询过滤器
    model = globals()[table_name]
    query = model.query

    # 使用 getattr() 函数获取属性
    filter_attr = getattr(model, attr, None)

    # 如果找到属性并且属性值不为空，就过滤并返回结果
    if filter_attr is not None and value:
        return query.filter(filter_attr == value).all()

    # 否则返回空结果
    return []


@get.route('/api/v1/<table_name>/<id>', methods=['GET'])
def get1_record(table_name, id):
    # print(str(globals()))
    model = globals()[table_name]

    # 根据 ID 查询要删除的记录
    record = None
    if table_name == 'departments':
        record = model.query.filter_by(dept_no=id).first()
    elif table_name == 'employees':
        record = model.query.filter_by(emp_no=int(id)).first()
    if not record:
        return jsonify({'error': 'Record not found.'}), 404
    # print(record.to_dict())
    return jsonify(record.to_dict()), 201


@get.route('/api/v1/<table_name>/<id1>/<id2>', methods=['GET'])
def get2_record(table_name, id1: int, id2: str):
    # print(str(globals()))
    model = globals()[table_name]

    # 根据 ID 查询要删除的记录
    record = None
    if table_name == 'dept_manager':
        record = model.query.filter_by(emp_no=id1, dept_no=id2).first()
    elif table_name == 'dept_emp':
        record = model.query.filter_by(emp_no=id1, dept_no=id2).first()
    if not record:
        return jsonify({'error': 'Record not found.'}), 404
    # print(record.to_dict())
    return jsonify(record.to_dict()), 201


@get.route('/api/v1/<table_name>/<id1>/<id2>/<id3>', methods=['GET'])
def get3_record(table_name, id1: int, id2: str, id3: str):
    # print(str(globals()))
    model = globals()[table_name]

    # 根据 ID 查询要删除的记录
    record = None
    if table_name == 'titles':
        record = model.query.filter_by(emp_no=id1, title=id2, from_date=id3).first()
    if not record:
        return jsonify({'error': 'Record not found.'}), 404
    # print(record.to_dict())
    return jsonify(record.to_dict()), 201


@get.route('/api/v1/<table_name>', methods=['GET'])
def get4_record(table_name):
    # print(str(globals()))

    attr_dict = request.args
    attr = list(attr_dict.keys())[0]
    ans = filter_by_attr(table_name, attr, attr_dict.get(attr))
    # record = filter_by_attr(table_name,)
    # if not record:
    #     return jsonify({'error': 'Record not found.'}), 404
    # print(record.to_dict())
    # print(ans)
    rc = []
    for a in ans:
        rc.append(a.to_dict())
    return jsonify(rc), 201
# return jsonify(record.to_dict()), 201
