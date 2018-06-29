from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel

# 管理员日志
class Adminlog(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    admin=relationship('Admin')
    admin_id=Column(Integer,ForeignKey('admin.id')) #管理员
    ip=Column(String(100)) #登陆ip