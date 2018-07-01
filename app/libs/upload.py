import datetime
import os
import uuid
from flask import current_app
from werkzeug.utils import secure_filename
# 文件上传类
class Upload_file:
    # 文件改名
    def __change_filename(self,filename):
        fileinfo=os.path.splitext(filename)
        filename=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[1]
        return filename
    #上次不同类型的文件给予不同目录
    def image(self,file):
        self.__upload_prex=current_app.config['UPLOADED_DIR']+'/image/'
        self.__static_dir=self.__upload_prex+datetime.datetime.now().strftime("%Y%m%d")+'/'
        self.__upload_path=current_app.config['UPLOADED_PATH']+self.__static_dir
        return self.__upload(file)

    # 上次不同类型的文件给予不同目录
    def video(self,file):
        self.__upload_prex = current_app.config['UPLOADED_DIR']+'/video/'
        self.__static_dir=self.__upload_prex+datetime.datetime.now().strftime("%Y%m%d")+'/'
        self.__upload_path = current_app.config['UPLOADED_PATH']+self.__static_dir
        return self.__upload(file)
    # 文件上传主要逻辑
    def __upload(self,file):
        # 安全验证文件名称
        file_secure_name=secure_filename(file.filename)
        # 判断上次文件夹是否存在，不存在则创建
        if not os.path.exists(self.__upload_path):
            os.makedirs(self.__upload_path)
            os.chmod(self.__upload_path,733)
        # 将上次文件改名
        filename=self.__change_filename(file_secure_name)
        # 用于保存文件，所以是绝对全路径
        save_path=self.__upload_path+filename
        # 用于返回，所以是相对路径
        return_path=self.__static_dir+filename
        # 保存文件
        try:
            file.save(save_path)
            return return_path
        except Exception as e:
            raise e
