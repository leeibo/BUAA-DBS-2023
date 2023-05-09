# 启用restful

请先对照`config.py`文件修改运行配置。比如：

```python
# config.py
config = {
    # 数据库地址
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://20376399:20376399@mysql.buaa.seekthought.com/db_20376399?charset'
                               '=utf8mb4',
    # csv数据源目录
    'shuJu': 'shuJu',
    # json数据源
    'jsons': 'jsons',
    # 数据请求url
    'url': "http://127.0.0.1:5000/api/v1/",
    # 分割符，在Linux下运行请改成'/',在windows环境下请改成'\\'
    'dot': '/'
}

```

默认使用docker，在此之前，请先使用`docker build -t flask-app .`来构建。

执行上述命令后，执行`start.sh`脚本即可启用部署在docker上的restful：`sh start.sh`

若不想启用docker服务，请修改`start.sh`相应注释。

```shell
# 不使用docker：	
# python main.py
# 使用docker，请先构建flask-app，可以使用如下命令
# docker build -t flask-app .
docker run -d -p 5000:5000 -v .:/app flask-app # 不使用docker请注释这一行
```

# 数据插入

请先修改`config.py`中数据集目录配置项。默认数据放在`shuJu`下

同样有两种插入模式：

不通过我们的restful接口插入可以直接运行脚本`sh insert.sh`。

若通过restful，请先打开restful服务，然后通过`python transform.py` 把csv转json后再`python inject.py`

实际上你也可以直接修改`insert.sh`文件中的相应注释：

```shell
# 选择是否通过restful服务注入数据
# 若通过restful注入，请先打开restful后使用以下命令：
# python transform.py && python inject.py
python inject_noRestful.py # 不使用restful注入请注释本行
```

然后`sh insert.sh`即可。