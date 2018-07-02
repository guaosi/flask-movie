from flask import render_template, request, flash, redirect, url_for, current_app

from app import db
from app.libs.enum import AdminTypeEnum
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.admin import Admin
from app.models.oplog import Oplog
from app.models.role import Role
from app.validators.admin import AdminAddForm

app=RedPrint()
@admin_login_required
@app.route('/admin/add',methods=['GET','POST'])
def admin_add():
    form=AdminAddForm(request.form)
    roles=Role.query.all()
    if request.method=='POST' and form.validate():
        with db.auto_commit():
            admin=Admin()
            admin.set_attr(form.data)
            admin.is_super=AdminTypeEnum.NO_SUPER
            db.session.add(admin)
            Oplog('添加管理员:' + admin.name)
            flash('添加管理员成功~','ok')
            return redirect(url_for('admin.admin_add'))
    return render_template('admin/admin_add.html',form=form,roles=roles)
@app.route('/admin/list/<int:page>')
@admin_login_required
def admin_list(page=None):
    if page is None:
        page=1
    admins=Admin.query.order_by(Admin.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_ADMIN_PAGE'])
    return render_template('admin/admin_list.html',admins=admins)