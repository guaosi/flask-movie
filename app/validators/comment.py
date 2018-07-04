from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, ValidationError

from app.models.movie import Movie


class CommentAddForm(FlaskForm):
    content=StringField(validators=[DataRequired('评论内容必须填写'),length(min=1,max=3000,message='评论内容过长~')])
    movie_id=IntegerField(validators=[DataRequired('电影状态不正确')])
    def validate_movie_id(self,field):
        movie=Movie.query.filter_by(id=field.data).first()
        if not movie:
            raise ValidationError('电影不存在~')