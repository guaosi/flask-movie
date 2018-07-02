from enum import Enum


class AdminTypeEnum(Enum):
    IS_SUPER=0
    NO_SUPER=1
    @classmethod
    def getAdminType(cls,type):
        key={
            cls.IS_SUPER:'超级管理员',
            cls.NO_SUPER:'普通管理员'
        }
        return key[type]