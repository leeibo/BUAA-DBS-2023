# 不使用docker：	
# python main.py
# 使用docker，请先构建flask-app，可以使用如下命令
# docker build -t flask-app .
docker run -d -p 5000:5000 -v .:/app flask-app # 不使用docker请注释这一行