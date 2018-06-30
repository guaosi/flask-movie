from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, length, ValidationError

from app.models.tag import Tag


class TagForm(FlaskForm):
    name=StringField(validators=[DataRequired('标签名称必须填写'),length(min=1,max=100,message='标签长度1~100之间')])
    def validate_name(self,field):
        if Tag.query.filter_by(name=field.data).first():
            raise ValidationError('标签已存在')


