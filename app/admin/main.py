from flask import render_template, redirect, url_for, request, flash, session

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.admin import Admin
from app.models.role import Role
from app.models.adminlog import Adminlog
from app.models.oplog import Oplog

from app.validators.main import LoginForm

app=RedPrint()
@app.route('/')
@admin_login_required
def index():
    return render_template('admin/index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if 'admin' in session:
        return redirect(url_for('admin.index'))
    form=LoginForm(request.form)
    if request.method=='POST' and form.validate():
        admin=Admin.query.filter_by(name=form.name.data).first()
        if admin and admin.check_hash_pwd(form.pwd.data):
            session['admin']=form.name.data
            url=request.args.get('next')
            if url is None:
                url=url_for('admin.index')
            return redirect(url)
        else:
            flash('账户不存在或者账户与密码不匹配')
    return render_template('admin/login.html',form=form)
@app.route('/logout')
@admin_login_required
def logout():
    session.pop('admin',None)
    return redirect(url_for('admin.login'))
