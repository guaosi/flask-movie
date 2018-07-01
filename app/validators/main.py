from flask import session
from wtforms import  StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm

from app.models.admin import Admin


class LoginForm(FlaskForm):
    name=StringField(validators=[DataRequired('账户必须填写'),Length(min=4,max=100,message='账户长度在4-100之间')])
    pwd=StringField(validators=[DataRequired('密码必须填写'),Length(min=4,max=100,message='密码长度在4-16之间')])
class PwdForm(FlaskForm):
    oldpwd=StringField(validators=[DataRequired('旧密码必须填写'),Length(min=4,max=16,message='密码长度在4-16之间')])
    newpwd=StringField(validators=[DataRequired('新密码必须填写'),Length(min=4,max=16,message='密码长度在4-16之间')])
    def validate_oldpwd(self,field):
        admin=Admin.query.filter_by(name=session['admin']).first()
        if not admin:
            raise ValidationError('当前管理员状态不正确')
        if not admin.check_hash_pwd(field.data):
            raise ValidationError('旧密码错误,请重新输入')
    def validate_newpwd(self,field):
        if field.data==self.oldpwd.data:
            raise ValidationError('新密码不能与旧密码相同~')