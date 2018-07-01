import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try: #开启事务
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
db=SQLAlchemy()
class BaseModel(db.Model):
    __abstract__=True
    addtime=Column(db.DateTime,index=True)
    #1
    def set_attr(self,attrs):
        for key,value in attrs.items():
            if hasattr(self,key) and key!='id':
                setattr(self,key,value)
    def __init__(self):
        self.addtime=datetime.datetime.now()