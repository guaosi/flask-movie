from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    name=StringField(validators=[DataRequired('账户必须填写'),Length(min=4,max=100,message='账户长度在4-100之间')])
    pwd=StringField(validators=[DataRequired('密码必须填写'),Length(min=4,max=100,message='密码长度在4-16之间')])