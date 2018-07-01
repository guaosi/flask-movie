from flask_uploads import IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import IntegerField, StringField, FileField
from wtforms.validators import DataRequired, length, ValidationError
from app.models.preview import Preview as PreviewModel

class Preview(FlaskForm):
    id=IntegerField()
    title=StringField(validators=[DataRequired('预告标题必须填写'),length(min=1,max=150,message='预告标题长度为1~150之间')])
    logo=FileField(validators=[FileRequired('预告图片必须上传'),FileAllowed(IMAGES, '图片格式不正确')])
class PreviewAddForm(Preview):
    def validate_title(self,field):
        preview=PreviewModel.query.filter_by(title=field.data).first()
        if preview:
            raise ValidationError('预告标题已存在')
class PreviewEditForm(Preview):
    logo=FileField(validators=[FileAllowed(IMAGES, '图片格式不正确')])
    def validate_title(self,field):
        preview=PreviewModel.query.filter(PreviewModel.id!=self.id.data,PreviewModel.title==field.data).first()
        if preview:
            raise ValidationError('预告标题已存在')