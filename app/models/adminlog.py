from flask import request
from sqlalchemy import Column, Integer, ForeignKey, String
from app.models.base import BaseModel, db


# 管理员日志
class Adminlog(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    admin_id=Column(Integer,ForeignKey('admin.id')) #管理员
    ip=Column(String(100)) #登陆ip
    def __init__(self,id):
        super(Adminlog, self).__init__()
        self.__add_log(id)
    def __add_log(self,id):
        self.admin_id=id
        self.ip=request.remote_addr
        with db.auto_commit():
            db.session.add(self)