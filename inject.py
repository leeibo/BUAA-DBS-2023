import requests
import json

from config import config
dot = config['dot']
jsons = config["jsons"]

filenames = ["departments.json", "employees.json", "dept_emp.json", "dept_manager.json", "titles.json"]
url = config["url"]
for filename in filenames:
    jsonfile = open(jsons + dot + filename, 'r', encoding='utf-8')
    data = json.load(jsonfile)
    jsonfile.close()  # 读取完毕后记得关闭文件
    print(jsons + dot + filename)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url + filename.split('.')[0], json=data, headers=headers)
    print(response.status_code)
