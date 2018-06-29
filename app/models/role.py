from sqlalchemy import Column, Integer, String
from app.models.base import BaseModel
# 角色
class Role(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    name=Column(String(100),unique=True) #角色名称
    auths=Column(String(600))