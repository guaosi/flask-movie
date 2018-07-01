import datetime

from flask import request, session
from sqlalchemy import Column, Integer, ForeignKey, String

from app.models.base import BaseModel, db


# 管理员操作日志
# 创建类即代表自动记录
class Oplog(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    admin_id=Column(Integer,ForeignKey('admin.id')) #管理员
    ip=Column(String(100)) #登陆ip
    reason=Column(String(150)) #操作原因
    def __init__(self,reson):
        super(Oplog, self).__init__()
        self.__add_log(reson)
    def __add_log(self,reason):
        self.reason=reason
        self.ip=request.remote_addr
        self.admin_id=session['admin_id']
        db.session.add(self)