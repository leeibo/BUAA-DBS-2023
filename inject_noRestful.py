import pandas as pd
from sqlalchemy import create_engine
from config import config
dot = config['dot']
filenames = ["departments.csv", "employees.csv", "dept_emp.csv", "dept_manager.csv", "titles.csv"]
# 连接数据库
engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])

# 读取CSV文件

shuJu = config["shuJu"]
for filename in filenames:
    df = pd.read_csv(shuJu + dot + filename)
    try:
        print(f"正在插入表格{filename}")
        file_path = shuJu + dot + filename
        csvfile = open(file_path, 'r', encoding='utf-8')
        if 'emp_no' in df.keys():
            df['emp_no'] = df['emp_no'].astype(int)
        # 将数据插入数据库中
        df.to_sql(filename.split('.')[0], con=engine, if_exists='append', index=False)
    except Exception as e:
        print(f"插入表格{filename}时出错！Exception{str(e)}")
