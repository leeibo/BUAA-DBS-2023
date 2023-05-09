from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)


class departments(db.Model):
    __tablename__ = 'departments'
    dept_no = db.Column(db.String(4), primary_key=True, nullable=False)
    dept_name = db.Column(db.String(40), nullable=False, unique=True)

    def __repr__(self):
        return '{<employees %r %r>}' % (self.first_name, self.last_name)

    def to_dict(self):
        return {'dept_no': self.dept_no, 'dept_name': self.dept_name}


# 定义 Employee 数据表
class employees(db.Model):
    __tablename__ = 'employees'
    emp_no = db.Column(db.Integer, primary_key=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(14), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    gender = db.Column(db.Enum('M', 'F'), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<employees %r %r>' % (self.first_name, self.last_name)

    def to_dict(self):
        return {'emp_no': self.emp_no, 'birth_date': self.birth_date, 'first_name': self.first_name,
                'last_name': self.last_name,
                'gender': self.gender, 'hire_date': self.hire_date}


# 定义 DeptEmp 数据表
class dept_emp(db.Model):
    __tablename__ = 'dept_emp'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True, nullable=False)
    dept_no = db.Column(db.String(4), db.ForeignKey('departments.dept_no'), primary_key=True, nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)

    #
    # employee = db.relationship('employee', backref=db.backref('department_assignments', lazy=True))
    # department = db.relationship('department', backref=db.backref('employee_assignments', lazy=True))

    def __repr__(self):
        return '<dept_emp %r %r>' % (self.emp_no, self.dept_no)

    def to_dict(self):
        return {'emp_no': self.emp_no, 'dept_no': self.dept_no, 'from_date': self.from_date, 'to_date': self.to_date}


# 定义 DeptManager 数据表
class dept_manager(db.Model):
    __tablename__ = 'dept_manager'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True, nullable=False)
    dept_no = db.Column(db.String(4), db.ForeignKey('departments.dept_no'), primary_key=True, nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)

    #
    # employee = db.relationship('employee', backref=db.backref('managed_department', lazy=True))
    # department = db.relationship('department', backref=db.backref('managers', lazy=True))

    def __repr__(self):
        return '<dept_manager %r %r>' % (self.emp_no, self.dept_no)

    def to_dict(self):
        return {'emp_no': self.emp_no, 'dept_no': self.dept_no, 'from_date': self.from_date, 'to_date': self.to_date}


# 定义 Titles 数据表
class titles(db.Model):
    __tablename__ = 'titles'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True, nullable=False)
    title = db.Column(db.String(50), primary_key=True, nullable=False)
    from_date = db.Column(db.Date, primary_key=True, nullable=False)
    to_date = db.Column(db.Date)

    # employee = db.relationship('employee', backref=db.backref('titles', lazy=True))

    def __repr__(self):
        return '<titles %r>' % self.title

    def to_dict(self):
        return {'emp_no': self.emp_no, 'title': self.title, 'from_date': self.from_date, 'to_date': self.to_date}


class DeptManagerTitle(db.Model):
    emp_no = db.Column(db.Integer, primary_key=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=True)

    def to_dict(self):
        return {'emp_no': self.emp_no, 'from_date': self.from_date, 'to_date': self.to_date}
