from flask_uploads import IMAGES, UploadSet
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from app.models.movie import Movie as MovieModel
from app.models.tag import Tag
class Movie(FlaskForm):
    id=IntegerField()
    title=StringField(validators=[DataRequired('电影标题必须填写'),Length(min=1,max=255,message='标题长度在1~255之间')])
    url=FileField(validators=[FileRequired('电影文件必须上传'),FileAllowed(['mp4', 'avi','mkv'], '视频格式不正确')])
    info=StringField(validators=[DataRequired('电影简介必须填写')])
    logo=FileField(validators=[FileRequired('电影文件必须上传'),FileAllowed(IMAGES, '图片格式不正确')])
    star=IntegerField(validators=[DataRequired('电影星级必须选择'),NumberRange(min=1,max=5,message='星级在1~5之间')])
    tag_id=IntegerField(validators=[DataRequired('电影标签必须选择')])
    release_time=DateField(validators=[DataRequired('电影上映时间必须选择')])
    length=StringField(validators=[DataRequired('电影时长必须选择')])
    area=StringField(validators=[DataRequired('电影上映地区必须选择')])
    def validate_title(self,field):
        tag=Tag.query.filter_by(id=field.data).first()
        if not tag:
            raise ValidationError('电影标题已存在')
class MovieAddForm(Movie):
    def validate_title(self,field):
        movie=MovieModel.query.filter_by(title=field.data).first()
        if movie:
            raise ValidationError('电影标题已存在')
    # def validate_url(self,field):
    #     movie=Movie.query.filter(title=field.data).first()
    #     if movie:
    #         raise ValidationError('电影地址已存在')
    # def validate_logo(self,field):
    #     movie=Movie.query.filter(title=field.data).first()
    #     if movie:
    #         raise ValidationError('电影封面已存在')
class MovieEditForm(Movie):
    pass