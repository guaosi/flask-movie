from sqlalchemy import Column, Integer, String, Text, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app.libs.enum import AdminTypeEnum
from app.models.base import BaseModel
# 管理员
class Admin(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    name=Column(String(100),unique=True) #管理员账号
    _pwd=Column('pwd',String(150)) #管理员密码
    _is_super=Column('is_super',SmallInteger) #是否为超级管理员 0为超级管理员
    adminlog=relationship('Adminlog',backref='admin')
    oplog=relationship('Oplog',backref='admin')
    role_id=Column(Integer,ForeignKey('role.id'))
    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self,raw):
        self._pwd=generate_password_hash(raw)
    def check_hash_pwd(self,raw):
        return check_password_hash(self._pwd,raw)
    @property
    def is_super(self):
        return AdminTypeEnum(self._is_super)
    @is_super.setter
    def is_super(self,raw):
        self._is_super=raw.value