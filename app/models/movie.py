from sqlalchemy import Column, Integer, String, Text, SmallInteger, BigInteger, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.models.base import BaseModel
# 电影
class Movie(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #编号
    title=Column(String(255),unique=True) #标题
    url=Column(String(255),unique=True) #地址
    info=Column(Text) #简介
    logo=Column(String(255),unique=True) #封面
    star=Column(SmallInteger) #星级
    playnum=Column(BigInteger) #播放量
    commentnum=Column(BigInteger) #评论量
    tag_id=Column(Integer,ForeignKey('tag.id')) #所属标签
    tag=relationship('Tag')
    area=Column(String(255)) #上映地球
    release_time=Column(Date) #上映时间
    length=Column(String(100)) #播放时长
    comment=relationship('Comment')