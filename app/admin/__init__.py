from flask import Blueprint
from app.admin import test
def create_admin_blueprint():
    bp=Blueprint('admin',__name__)
    test.app.register(bp,url_prefix='/admin')
    return bp