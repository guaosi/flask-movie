from functools import wraps
from flask import session, redirect, url_for, request, abort
# 后台登陆检测装饰器
from app.libs.enum import AdminTypeEnum
from app.models.admin import Admin
from app.models.auth import Auth


def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login',next=request.url))
        return f(*args,**kwargs)
    return decorated_function

# 后台权限检测装饰器

def admin_auth(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        rule=str(request.url_rule)
        admin = Admin.query.filter_by(name=session['admin']).first()
        #首页无需验证直接跳转
        if admin.is_super != AdminTypeEnum.IS_SUPER and rule!='/admin/' :
            auths=[int(v) for v in admin.role.auths.split(',')]
            auth_url=['/admin'+auth.url for auth in Auth.query.filter(Auth.id.in_(auths)).all()]
            if rule not in auth_url:
                abort(404)
        return f(*args,**kwargs)
    return decorated_function