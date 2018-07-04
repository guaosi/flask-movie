from flask_login import current_user
from flask_uploads import IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import IntegerField, StringField, FileField
from wtforms.validators import DataRequired, length, EqualTo, Email, Regexp, ValidationError

from app.models.user import User


class UserForm(FlaskForm):
    name=StringField(validators={DataRequired('用户名必须填写'),length(min=1,max=20,message='用户名长度在1-20之间')})
class UserRegisterForm(UserForm):
    email = StringField(validators=[DataRequired('邮箱必须填写'),Email(message='邮箱格式不正确')])
    pwd=StringField(validators={DataRequired('密码必须填写'),length(min=1,max=16,message='密码长度在1-16之间')})
    phone = StringField(validators=[DataRequired('手机号码必须填写'),Regexp("1[3458]\\d{9}",message='手机格式不正确')])
    repwd=StringField(validators={DataRequired('重复密码必须填写'),length(min=1,max=16,message='重复密码长度在1-100之间'),EqualTo('pwd')})
    def validate_name(self,field):
        user=User.query.filter_by(name=field.data).first()
        if user:
            raise ValidationError('用户名已存在')
    def validate_email(self,field):
        user=User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('邮箱已存在')
    def validate_phone(self,field):
        user=User.query.filter_by(phone=field.data).first()
        if user:
            raise ValidationError('手机号已存在')
class UserLoginForm(UserForm):
    name=StringField(validators={DataRequired('用户名必须填写'),length(min=1,max=20,message='用户名长度在1-20之间')})
    pwd=StringField(validators={DataRequired('密码必须填写'),length(min=1,max=16,message='密码长度在1-166之间')})
class UserEditForm(UserForm):
    face = FileField(validators=[FileAllowed(IMAGES, '图片格式不正确')])
    email = StringField(validators=[DataRequired('邮箱必须填写'),Email(message='邮箱格式不正确')])
    phone = StringField(validators=[DataRequired('手机号码必须填写'),Regexp("1[3458]\\d{9}",message='手机格式不正确')])
    info = StringField()

    def validate_name(self, field):
        id=current_user.id
        user = User.query.filter(User.id!=id,User.name==field.data).first()
        if user:
            raise ValidationError('用户名已存在')

    def validate_email(self, field):
        id = current_user.id
        user = User.query.filter(User.id!=id,User.email==field.data).first()
        if user:
            raise ValidationError('邮箱已存在')

    def validate_phone(self, field):
        id = current_user.id
        user = User.query.filter(User.id!=id,User.phone==field.data).first()
        if user:
            raise ValidationError('手机号已存在')
class UserPwdForm(FlaskForm):
    pwd=StringField(validators={DataRequired('旧密码必须填写'),length(min=1,max=16,message='旧密码长度在1-16之间')})
    newpwd=StringField(validators={DataRequired('新密码必须填写'),length(min=1,max=16,message='新密码长度在1-16之间')})
    def validate_pwd(self,field):
        user=current_user._get_current_object()
        if not user.check_hash_pwd(field.data):
            raise ValidationError('旧密码不正确~')
    def validate_newpwd(self,field):
        user=current_user._get_current_object()
        if user.check_hash_pwd(field.data):
            raise ValidationError('新密码不能与旧密码相同~')

