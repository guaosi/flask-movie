from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, length, ValidationError
from app.models.auth import Auth as AuthModel

class Auth(FlaskForm):
    id=IntegerField()
    name=StringField(validators={DataRequired('权限名称必须填写'),length(min=1,max=20,message='权限名称长度在1-20之间')})
    url=StringField(validators={DataRequired('权限地址必须填写'),length(min=1,max=100,message='权限地址长度在1-100之间')})
class AuthAddForm(Auth):
    def validate_name(self,field):
        auth=AuthModel.query.filter_by(name=field.data).first()
        if auth:
            raise ValidationError('权限名称已经存在')
    def validate_url(self,field):
        auth=AuthModel.query.filter_by(url=field.data).first()
        if auth:
            raise ValidationError('权限地址已经存在')
class AuthEditForm(Auth):
    def validate_name(self,field):
        auth=AuthModel.query.filter(AuthModel.id!=self.id.data,AuthModel.name==field.data).first()
        if auth:
            raise ValidationError('权限名称已经存在')
    def validate_url(self,field):
        auth=AuthModel.query.filter(AuthModel.id!=self.id.data,AuthModel.url==field.data).first()
        if auth:
            raise ValidationError('权限地址已经存在')