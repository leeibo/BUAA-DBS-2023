# 使用官方的 Python 3.9 镜像作为基础镜像
FROM python:3.9

# 将 Flask 应用程序文件复制到容器中
WORKDIR /app
COPY . /app

# 安装依赖
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 暴露端口
EXPOSE 5000

# 设定环境变量
ENV FLASK_ENV=production

# 执行命令，启动 Flask 应用程序
CMD ["python", "main.py"]