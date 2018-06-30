from wtforms import  StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
class LoginForm(FlaskForm):
    name=StringField(validators=[DataRequired('账户必须填写'),Length(min=4,max=100,message='账户长度在4-100之间')])
    pwd=StringField(validators=[DataRequired('密码必须填写'),Length(min=4,max=100,message='密码长度在4-16之间')])
    # submit=SubmitField('登陆',render_kw={
    #     'class':"btn btn-primary btn-block btn-flat"
    # })