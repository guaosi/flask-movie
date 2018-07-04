from flask import Flask
from flask_wtf.csrf import CSRFProtect, CsrfProtect
from app.models.base import db
from flask_login import LoginManager
from flask_redis import FlaskRedis
login_manager = LoginManager()
rd = FlaskRedis()
csrf = CSRFProtect()
def create_app():
    app=Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    login_manager.init_app(app)
    login_manager.login_view='home.login' #没有登录时候的跳转地址
    login_manager.login_message='请先进行登陆'#没有登录时候的闪现信息
    login_manager.login_message_category='err'
    register_blueprint(app)
    # 注册redis
    rd.init_app(app)
    register_db(app)
    # csrf保护
    csrf.init_app(app)
    return app
def register_blueprint(app):
    from app.home import create_home_blueprint as r1
    from app.admin import create_admin_blueprint as r2
    app.register_blueprint(r1())
    app.register_blueprint(r2())
def register_db(app):
    # 注册SQLAlchemy
    db.init_app(app)
    # with app.app_context()
    db.create_all(app=app)