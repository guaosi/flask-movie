from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, length, ValidationError, EqualTo
from app.models.admin import Admin as AdminModel
from app.models.role import Role


class Admin(FlaskForm):
    id=IntegerField()
    name=StringField(validators={DataRequired('管理员名称必须填写'),length(min=1,max=20,message='管理员名称长度在1-20之间')})
    pwd=StringField(validators={DataRequired('密码必须填写'),length(min=1,max=16,message='密码长度在1-100之间')})
    repwd=StringField(validators={DataRequired('重复密码必须填写'),length(min=1,max=16,message='重复密码长度在1-100之间'),EqualTo('pwd')})
    role_id=IntegerField(validators={DataRequired('角色必须选择')})
class AdminAddForm(Admin):
    def validate_name(self,field):
        admin=AdminModel.query.filter_by(name=field.data).first()
        if admin:
            raise ValidationError('名称已经存在')
    def validate_role_id(self,field):
        role=Role.query.filter_by(id=field.data).first()
        if not role:
            raise ValidationError('所选角色不存在')