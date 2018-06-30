from functools import wraps
from flask import session, redirect, url_for, request
# 后台登陆检测装饰器
def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login',next=request.url))
        return f(*args,**kwargs)
    return decorated_function