from flask import render_template, request, flash, current_app, redirect, url_for
from werkzeug.datastructures import MultiDict, CombinedMultiDict

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.auth import Auth
from app.models.oplog import Oplog
from app.validators.auth import AuthAddForm, AuthEditForm

app=RedPrint()

@app.route('/auth/add',methods=['GET','POST'])
@admin_login_required
def auth_add():
    form=AuthAddForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            auth=Auth()
            auth.set_attr(form.data)
            db.session.add(auth)
            Oplog('添加权限:' + auth.name)
            flash('添加权限成功~','ok')
            return redirect(url_for('admin.auth_add'))
    return render_template('admin/auth_add.html',form=form)
@app.route('/auth/list/<int:page>')
@admin_login_required
def auth_list(page=None):
    if page is None:
        page=1
    auths=Auth.query.order_by(Auth.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_AUTH_PAGE'])
    return render_template('admin/auth_list.html',auths=auths)
@app.route('/auth/del/<int:id>')
@admin_login_required
def auth_del(id):
    auth=Auth.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除权限:' + auth.name + ',id:' + str(auth.id))
        db.session.delete(auth)
        flash('删除权限成功~','ok')
        return redirect(url_for('admin.auth_list',page=1))

@app.route('/auth/edit/<int:id>',methods=['GET','POST'])
@admin_login_required
def auth_edit(id):
    id_dict=MultiDict([('id',id)])
    values=CombinedMultiDict([id_dict, request.form])
    auth=Auth.query.get_or_404(id)
    form=AuthEditForm(values)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            auth.set_attr(form.data)
            db.session.add(auth)
            Oplog('修改权限:' + auth.name + ',id:' + str(auth.id))
            flash('修改权限成功~','ok')
            return redirect(url_for('admin.auth_edit',id=id))
    return render_template('admin/auth_edit.html',form=form,auth=auth)
