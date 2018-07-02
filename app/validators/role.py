from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectMultipleField
from wtforms.validators import DataRequired, length, ValidationError
from app.models.role import Role as RoleModel

class Role(FlaskForm):
    id=IntegerField()
    name=StringField(validators={DataRequired('角色名称必须填写'),length(min=1,max=20,message='角色名称长度在1-20之间')})
    auths=StringField(validators={DataRequired('拥有权限不能为空')})
class RoleAddForm(Role):
    def validate_name(self,field):
        role=RoleModel.query.filter_by(name=field.data).first()
        if role:
            raise ValidationError('角色名称已经存在')
class RoleEditForm(Role):
    def validate_name(self,field):
        role=RoleModel.query.filter(RoleModel.id!=self.id.data,RoleModel.name==field.data).first()
        if role:
            raise ValidationError('角色名称已经存在')