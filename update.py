from flask import Blueprint
from Model import *

update = Blueprint('update', __name__)


@update.route('/api/v1/<table_name>', methods=['PUT'])
def update_data(table_name):
    # datas = request.json['rows']
    datas = request.json
    if table_name == 'departments':
        primary_key = 'dept_no'
    elif table_name == 'employees':
        primary_key = 'emp_no'
    elif table_name == 'dept_emp':
        primary_key = ('emp_no', 'dept_no')
    elif table_name == 'dept_manager':
        primary_key = ('emp_no', 'dept_no')
    elif table_name == 'titles':
        primary_key = ('emp_no', 'title', 'from_date')
    else:
        return jsonify({'error': 'Unknown table name'})
    model = globals()[table_name]
    data = request.json
    # for data in datas:
    filter_dict = {}
    if isinstance(primary_key, str):
        filter_dict[primary_key] = data[primary_key]
    elif isinstance(primary_key, tuple):
        for key in primary_key:
            filter_dict[key] = data[key]
    record = model.query.filter_by(**filter_dict).first()
    if record is None:
        return jsonify({'error': 'Record not found'})
    property_list = [p for p in vars(model) if not p.startswith('__')]
    for key, value in data.items():
        if key not in filter_dict:
            if key not in property_list:
                return jsonify({'error': f'Attribute {key} not found'})
            setattr(record, key, value)
    db.session.commit()
    return jsonify({'message': f'1 row undate into {table_name} successfully',
                    "updated line": record.to_dict()}), 201
