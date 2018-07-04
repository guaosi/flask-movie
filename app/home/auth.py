import uuid

from flask import render_template, url_for, redirect, request, flash

from app import db
from app.libs.redprint import RedPrint
from app.models.user import User
from app.models.userlog import Userlog
from app.validators.user import UserRegisterForm, UserLoginForm
from flask_login import login_user, logout_user, current_user, login_required

app=RedPrint()
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index',page=1))
    form=UserLoginForm(request.form)
    if request.method=='POST' and form.validate():
        user=User.verify(form.name.data,form.pwd.data)
        if not user:
            flash('用户名不存在或者与密码不匹配','err')
            return redirect(url_for('home.login'))
        login_user(user)
        Userlog()
        url = request.args.get('next')
        if not url or not url.startswith('/'):
            # 如果next被恶意修改，导致重定向攻击，此时可以判断 url的第一个字符是否是 '/'
            url = url_for('home.index',page=1)
        return redirect(url)
    return render_template('home/login.html',form=form)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.login'))
@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index',page=1))
    form=UserRegisterForm(request.form)
    if request.method=='POST' and form.validate():
        with db.auto_commit():
            user=User()
            value=form.data
            value['face']="avatar/1.jpg"
            value['uuid']=str(uuid.uuid4().hex)
            user.set_attr(value)
            db.session.add(user)
            flash('注册成功','ok')
            return redirect(url_for('home.login'))
    return render_template('home/register.html',form=form)