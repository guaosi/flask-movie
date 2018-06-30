from sqlalchemy import Column, Integer, ForeignKey, Text
from app.models.base import BaseModel

# 电影评论
class Comment(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    content=Column(Text) #评论内容
    user_id=Column(Integer,ForeignKey('user.id')) #用户
    movie_id=Column(Integer,ForeignKey('movie.id')) #电影
