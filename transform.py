import csv
import json
import os
from config import config
dot = config['dot']
shuJu = config["shuJu"]
jsons = config["jsons"]
filenames = os.listdir(shuJu)
for filename in filenames:
    try:
        print(f"正在转化表格{filename}")
        file_path = shuJu + dot + filename
        csvfile = open(file_path, 'r', encoding='utf-8')
        jsonfile = open(jsons + dot + filename.split('.')[0] + '.json', 'w', encoding='utf-8')
        # 指定列名
        readers = csv.DictReader(csvfile)

        rows = list(readers)
        # 指定ensure_ascii=False 为了不让中文显示为ascii字符码
        tdict = {
            "table_name": filename.split('.')[0],
            "rows": rows
        }
        json.dump(tdict, jsonfile)
    except Exception as e:
        print(f"转化表格{filename}时出错！Exception{str(e)}")
