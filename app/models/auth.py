from sqlalchemy import Column, Integer, String
from app.models.base import BaseModel
# 权限
class Auth(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    name=Column(String(100),unique=True) #权限名称
    url=Column(String(150),unique=True) #地址