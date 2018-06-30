# 离线脚本，创建超级管理员
from app import create_app
from app.libs.enum import AdminTypeEnum
from app.models.admin import Admin
from app.models.base import db

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        admin = Admin()
        admin.name = 'admin'
        admin.pwd = 'a123654'
        admin.is_super=AdminTypeEnum.IS_SUPER
        db.session.add(admin)
