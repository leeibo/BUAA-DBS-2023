from sqlalchemy import text
from get import get
from insert import insert
from update import update
from delete import delete
from Model import app, db

app.register_blueprint(get)
app.register_blueprint(insert)
app.register_blueprint(delete)
app.register_blueprint(update)

if __name__ == '__main__':

    with app.app_context():
        # 在应用上下文中运行数据库操作
        db.create_all()
        try:
            db.session.execute(text("""
                CREATE TRIGGER tr_dept_manager_insert AFTER INSERT ON dept_manager
                FOR EACH ROW BEGIN
                    INSERT INTO dept_manager_title (emp_no, from_date, to_date)
                    VALUES (NEW.emp_no, NEW.from_date, NEW.to_date);
                END"""))
            db.session.execute(text("""
                               CREATE TRIGGER tr_dept_manager_delete AFTER DELETE ON dept_manager
                               FOR EACH ROW BEGIN
                                   DELETE FROM dept_manager_title WHERE emp_no = OLD.emp_no;
                               END"""))
        except Exception as e:
            print("Trigger already exists")

        db.session.commit()
    app.run(debug=True, use_reloader=False)
