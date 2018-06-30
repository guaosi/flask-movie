from sqlalchemy import Column, Integer, String

from app.models.base import BaseModel
# 上映预告
class Preview(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    title=Column(String(150),unique=True) #标题
    logo=Column(String(150),unique=True) #封面