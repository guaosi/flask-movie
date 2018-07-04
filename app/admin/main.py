from flask import render_template, redirect, url_for, request, flash, session

from app import db
from app.libs.login import admin_login_required,admin_auth
from app.libs.redprint import RedPrint
from app.models.admin import Admin
from app.models.role import Role
from app.models.adminlog import Adminlog
from app.models.oplog import Oplog

from app.validators.main import LoginForm, PwdForm

app=RedPrint()
@app.route('/')
@admin_login_required
@admin_auth
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
            session['admin']=admin.name
            session['admin_id']=admin.id
            Adminlog(admin.id)
            url=request.args.get('next')
            if url is None:
                url=url_for('admin.index')
            return redirect(url)
        else:
            flash('账户不存在或者账户与密码不匹配','err')
    return render_template('admin/login.html',form=form)
@app.route('/logout')
@admin_login_required
def logout():
    session.pop('admin',None)
    return redirect(url_for('admin.login'))
@app.route('/pwd',methods=['GET','POST'])
@admin_login_required
def pwd():
    form=PwdForm(request.form)
    if request.method=='POST' and form.validate():
        admin=Admin.query.filter_by(name=session['admin']).first()
        with db.auto_commit():
            admin.pwd=form.newpwd.data
            db.session.add(admin)
            Oplog('修改密码:' + admin.name + ',id:' + str(admin.id))
            flash('密码修改成功,请重新登陆','ok')
            return redirect(url_for('admin.logout'))
    return render_template('admin/pwd.html',form=form)
