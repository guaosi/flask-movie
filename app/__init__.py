from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.models.base import db
from flask_login import LoginManager
login_manager = LoginManager()
def create_app():
    app=Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    login_manager.init_app(app)
    login_manager.login_view='home.login' #没有登录时候的跳转地址
    login_manager.login_message='请先进行登陆'#没有登录时候的闪现信息
    login_manager.login_message_category='err'
    register_blueprint(app)
    register_db(app)
    # csrf保护
    CSRFProtect(app)
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