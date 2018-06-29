from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from app.models.base import BaseModel

# 电影评论
class Comment(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    content=Column(Text) #评论内容
    user=relationship('User')
    user_id=Column(Integer,ForeignKey('user.id')) #用户
    movie=relationship('Movie')
    movie_id=Column(Integer,ForeignKey('movie.id')) #电影
