from sqlalchemy import Column, Integer, String, Text, SmallInteger
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import BaseModel
# 管理员
class Admin(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    name=Column(String(100),unique=True) #管理员账号
    _pwd=Column('pwd',String(256)) #管理员密码
    is_super=Column(SmallInteger) #是否为超级管理员 0为超级管理员
    role=relationship('Role')
    adminlog=relationship('Adminlog')
    oplog=relationship('Oplog')
    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self,raw):
        self._pwd=generate_password_hash(raw)
    def check_hash_pwd(self,raw):
        return check_password_hash(self._pwd,raw)