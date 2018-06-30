from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import BaseModel
# 用户
class User(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    name=Column(String(100),unique=True) #用户名
    _pwd=Column('pwd',String(150)) #密码
    email=Column(String(100),unique=True) #电子邮箱
    phone=Column(String(11),unique=True) #号码
    info=Column(Text) #个人简介
    face=Column(String(150),unique=True) #头像
    uuid=Column(String(150),unique=True) #唯一标志符
    userlog=relationship('Userlog')
    moviecol=relationship('MovieCol')
    comment=relationship('Comment',backref='user')
    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self,raw):
        self._pwd=generate_password_hash(raw)
    def check_hash_pwd(self,raw):
        return check_password_hash(self._pwd,raw)