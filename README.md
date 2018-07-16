基于flask构建微电影网站，已部署测试(附线上部署过程)，增加异步功能，项目结构优化，发送弹幕，速率控制
===============
> 🚀 结合先前的flask-yushu和flask-api来构建的前后台，项目结构可以参考。


**已经部署到 Linux+mysql+nginx+uwsgi 环境中,下面会有教程**

# 特性

- 基于蓝图创建红图,更好细分模块与视图函数

- 稍微完善的后台权限

- 自定义登陆检测装饰器与权限检测装饰器

- 多线程异步增加评论与访问数量

- 结合redis实现弹幕发送

- 使用with的上下文特性自动开启事务

- flask-login处理前台登陆逻辑

- 使用Enum枚举类来表示状态，更具可读性

- csrf认证

- WTForms参数验证

- Jinja2模板引擎

- 基于SQLAlchemy的CRUD

- 简单，开箱即用

> Python的运行环境要求3.6以上。

**学生服务器1G内存部署PHP项目已经不够用了，这个项目无法给测试网址了**

# 要求

| 依赖 | 说明 |
| -------- | -------- |
| Python| `>= 3.6` |
| Flask| `>= 1.0.2` |
| cymysql| `>= 0.9.10` |
| Flask-Login |`>= 0.4.1`|
| Flask-Redis |`>= 0.3.0`|
| Flask-SQLAlchemy  |`>= 2.3.2`|
| itsdangerous |`>= 0.24`|
| Jinja2 |`>= 2.10`|
| requests |`>= 2.18.4`|
| SQLAlchemy  |`>= 1.2.8`|
| Werkzeug |`>= 0.14.1`|
| WTForms |`>= 2.2`|

# 注意

1. 数据库在运行movie.py自动生成,请手动将每个数据表的引擎改为Innodb,默认为MyISAM,无事务功能。

2. 需要在app目录下创建secure.py文件。

3. **flask扩展需要自行安装**

4. 必须安装redis，否则弹幕功能无效
>安装redis可以参考我yii2-shop的readme  https://github.com/guaosi/yii2-shop

5. 测试部署上线成功，本文会给部署过程

# 安装

1. 通过[Github](https://github.com/guaosi/flask-movie),fork到自己的项目下
```
git clone git@github.com:<你的用户名>/flask-movie.git
```
2. 在app/config目录下创建secure.py文件
```
DEBUG=True  #是否开启Dubug
HOST='0.0.0.0' #0.0.0.0表示访问权限为全网
PORT=80 #访问端口号

# mysql连接，比如 SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:root@localhost:3306/movie'
SQLALCHEMY_DATABASE_URI='mysql+cymysql://用户名:用户名@ip地址:mysql端口号/数据库名'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SECRET_KEY='任意字符串作为你的秘钥key'
# redis服务器地址  比如  REDIS_URL = "redis://127.0.0.1:6379/10"
REDIS_URL = "redis://你的redis服务器地址:6379/redis里的第几个db"
```
3. 根目录下的 fake.py文件，可以生成管理员账户和前台用户。这次给了我本地的测试数据库，可以跳过这步。

4. 因为git里我忽略了上传upload文件夹，所以头像影片不会上传，需要自行到后台添加一下。

## 相关依赖

最好在pipenv的虚拟环境中安装，避免全局污染,确保pipFile文件存在。根据Pipfile自动安装所有依赖。
```
pipenv install
```

## 运行

> `python movie.py`

# 项目中的使用

## 在项目中注册路由

前后台部分(home,admin)已经用红图代替了蓝图。

如果是**前台**。在 app/home 下构建 视图(比如test).py文件后，需要到app/home/\_\_init.py\_\_文件中进行注册。比如
```
from flask import Blueprint
from app.home import test
bp = Blueprint('home',__name__)
def create_home_blueprint():
    test.app.register(bp)
    return bp
```
如果 视图(比如test).py文件中注册是视图函数route是
```
from app.libs.redprint import Redprint
app=RedPrint()
@app.route('/test')
def test():
    return 'test'
```
此时API接口地址应为
> http://localhost/test

如果是**后台**。在 app/admin 下构建 视图(比如test).py文件后，需要到app/admin/\_\_init.py\_\_文件中进行注册。比如
```
from flask import Blueprint
from app.admin import test
bp=Blueprint('admin',__name__)
def create_home_blueprint():
    test.app.register(bp,url_prefix='/admin')
    return bp
```
如果 视图(比如test).py文件中注册是视图函数route是
```
from app.libs.redprint import Redprint
app=RedPrint()
@app.route('/test')
def test():
    return 'test'
```
此时API接口地址应为
> http://localhost/admin/test

## 在项目中使用事务

已经使用with和yield对事务做了上下文处理，当进行数据库处理时，请在with下操作，发生错误时自动回滚
```
with db.auto_commit():
    # orm逻辑
    db.session.add(模型实例)
```

# 测试账号与密码

以上都完成后 前后台登录账号密码

admin a123654

前台地址:

http://你的网址/1/

后台地址:

http://你的网址/admin

# 部署上线云服务器

| 依赖 | 说明 |
| -------- | -------- |
| Centos| `>= 7.2` |
| Python| `>= 3.6` |
| Flask| `>= 1.0.2` |
| MySQL或者MariaDB| `>= 5.5` |
| nginx |`>= 1.4.0`|
| uwsgi |`>= 2.0.17`|
| pipenv | 暂无 |


**参考了很多文章，部署了差不多2个小时，成功。下面将我测试时候没问题的文章会直接给链接参考，有问题有坑的会特别说明**

## 安装Python3

Centos7内置了Python2.7版本,yum要使用Python2.7，所以不能将内置的Python2.7卸载，而是进行兼容。
安装Python3并且兼容参考:

> https://www.cnblogs.com/JahanGu/p/7452527.html

不要忘记先安装依赖包

```
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make
```

## 安装Pip

根据上一节安装完成Python3后，Python内置了Pip，不过Centos7也内置了基于Python2.7的Pip,需要进行替换。

```
rm -rf /usr/bin/pip
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip
```

## 安装MySQL

centos7以上版本将MySQL替换为了MariaDB,不过这2个数据库是同一个作者，语法完全一样，完全兼容，这边为了方便，直接安装内置的MariaDB。
安装MariaDB参考:

> https://blog.csdn.net/junehappylove/article/details/77508932

安装完成后，记得创建movie数据库，导入项目中的movie.sql文件

## 安装Nginx

nginx没有什么特殊限制，下一个能用的就行了

安装Nginx参考:

> https://blog.csdn.net/stinkstone/article/details/78082748

完成后请务必测试能否访问成功~成功后再进行后面的步骤

## 安装pipenv

使用pipenv来构建虚拟化环境

> pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com pipenv

## 安装项目

建议将项目安装在 /home/www 目录下

> 比如 /home/www/movie/movie.py 下面步骤以这个为例

将github上的项目git clone 下来或者在本地压缩传到服务器上解压。
记得创建secure.py文件，具体配置看上面的 安装 部分。

以下步骤都是已经
```
cd /home/www/movie
```
并且是movie的项目目录，比如现在movie.py目前所在的目录是

> /home/www/movie/movie.py 下面步骤以这个为例

1. 进入到项目目录后,执行

> pipenv install --python=3.6

会自动创建虚拟化环境，根据Pipfile自动安装所有依赖。

2. 进入虚拟化环境

> pipenv shell

3. 安装uwsgi

> pipenv install uwsgi

4. 配置uwsgi

创建 uwsgi.ini
```
vim uwsgi
```
写入以下内容
```
[uwsgi]

http = 0.0.0.0:8080 #0.0.0.0代表可以全网访问，端口为8080

chdir = /home/www/movie/ #项目目录

wsgi-file = movie.py #项目启动文件

callable = app #flask核心对象

processes = 1 #进程数

threads = 2 #线程数
```
启动uwsgi
> uwsgi uwsgi.ini

此时测试网址
 
 > http://公网IP:8080/1/ 
 
 能否正常访问，可以则代表uswgi成功

注意，这里配置的是http，用于直接测试，后面nginx代理转发给uwsgi则需要改为socket

## nginx代理转发

```
vim /usr/local/nginx/conf/nginx.conf
```
参考配置如下
```
    server {
        listen       80;
        server_name  公网IP;

        #server_name  localhost;
        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            #root   html;
            #index  index.html index.htm;
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8080; #转发uwsgi
            uwsgi_param UWSGI_PYHOME /home/www/movie; # 指向虚拟环境目录
            uwsgi_param UWSGI_CHDIR  /home/www/movie; # 指向网站根目录
            uwsgi_param UWSGI_SCRIPT movie:app; # 指定启动程序
        }
```

此时，重启nginx以及uwsgi。

测试网址
 
> http://公网IP/1/ 

能否正常访问，可以则代表代理转发成功

## nginx访问限制
```
vim /usr/local/nginx/conf/nginx.conf
```
参考配置如下
```
http {
    include       mime.types;
    default_type  application/octet-stream;
    limit_conn_zone $binary_remote_addr zone=addr:10m; #用于限制单个ip访问定义
    client_max_body_size 50m; #用于设置上传文件大小
    ```
    ```
    ```
 server {
        listen       80;
        server_name  公网IP;

        #server_name  localhost;
        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            #root   html;
            #index  index.html index.htm;
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8080; #转发uwsgi
            uwsgi_param UWSGI_PYHOME /home/www/movie; # 指向虚拟环境目录
            uwsgi_param UWSGI_CHDIR  /home/www/movie; # 指向网站根目录
            uwsgi_param UWSGI_SCRIPT movie:app; # 指定启动程序
        }
        # 对.flv的格式视频做限制
        location ~ \.flv$ {
            limit_conn addr 1; #用于限制每个IP每次请求的数量
            limit_rate 1024k; #用于限制每个IP每次请求的大小
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8080; #转发uwsgi
            uwsgi_param UWSGI_PYHOME /home/www/movie; # 指向虚拟环境目录
            uwsgi_param UWSGI_CHDIR  /home/www/movie; # 指向网站根目录
            uwsgi_param UWSGI_SCRIPT movie:app;              
            }
        # 对.mp4的格式视频做限制
        location ~ \.mp4$ {
            limit_conn addr 1; #用于限制每个IP每次请求的数量
            limit_rate 1024k;  #用于限制每个IP每次请求的大小
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8080; #转发uwsgi
            uwsgi_param UWSGI_PYHOME /home/www/movie; # 指向虚拟环境目录           
            uwsgi_param UWSGI_CHDIR  /home/www/movie; # 指向网站根目录            
            uwsgi_param UWSGI_SCRIPT movie:app;                }

```


