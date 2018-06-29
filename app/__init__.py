from flask import Flask

from app.models.base import db


def create_app():
    app=Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprint(app)
    register_db(app)
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