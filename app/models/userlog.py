from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel

# 用户日志
class Userlog(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    user_id=Column(Integer,ForeignKey('user.id')) #用户
    ip=Column(String(100)) #登陆ip