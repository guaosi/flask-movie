# 离线脚本，创建超级管理员
import uuid

from app import create_app
from app.libs.enum import AdminTypeEnum
from app.models.admin import Admin
from app.models.base import db
from app.models.user import User
from app.models.userlog import Userlog
from app.models.moviecol import MovieCol
from app.models.comment import Comment

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        admin_exists=Admin.query.filter_by(name='admin').first()
        if not admin_exists:
            admin = Admin()
            admin.name = 'admin'
            admin.pwd = 'a123654'
            admin.is_super=AdminTypeEnum.IS_SUPER
            db.session.add(admin)
    for v in range(1, 4):
        with db.auto_commit():
            user=User()
            user.name='guaosi'+str(v)
            user.pwd='a123654'
            user.email='guaosi'+str(v)+'@guaosi.com'
            user.phone='1234567891'+str(v)
            user.info='这是个人简介'
            user.face='avatar/'+str(v)+'.jpg'
            user.uuid=str(uuid.uuid4().hex)
            db.session.add(user)

