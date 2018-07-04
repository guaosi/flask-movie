from flask import request
from flask_login import current_user
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel, db


# 用户日志
class Userlog(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    user_id=Column(Integer,ForeignKey('user.id')) #用户
    ip=Column(String(100)) #登陆ip
    def __init__(self):
        super(Userlog, self).__init__()
        self.__add_log()
    def __add_log(self):
        self.ip=request.remote_addr
        self.user_id=current_user.id
        with db.auto_commit():
            db.session.add(self)