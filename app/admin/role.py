from flask import render_template, request, flash, redirect, url_for, current_app
from werkzeug.datastructures import MultiDict, CombinedMultiDict

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.auth import Auth
from app.models.oplog import Oplog
from app.models.role import Role
from app.validators.role import RoleAddForm, RoleEditForm

app=RedPrint()
@app.route('/role/add',methods=['GET','POST'])
@admin_login_required
def role_add():
    auth_list = request.values.getlist("auths")
    auth_list=list_to_str(auth_list)
    id_dict=MultiDict([('auths',auth_list)])
    values=CombinedMultiDict([id_dict, request.form])
    form=RoleAddForm(values)
    auths=Auth.query.all()
    if request.method=='POST' and form.validate():
        with db.auto_commit():
            role=Role()
            role.set_attr(form.data)
            db.session.add(role)
            Oplog('添加角色:' + role.name)
            flash('添加角色成功~','ok')
            return redirect(url_for('admin.role_add'))
    return render_template('admin/role_add.html',auths=auths,form=form)
@app.route('/role/list/<int:page>')
@admin_login_required
def role_list(page=None):
    if page is None:
        page=1
    roles=Role.query.order_by(Role.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_ROLE_PAGE'])
    return render_template('admin/role_list.html',roles=roles)


@app.route('/role/del/<int:id>')
@admin_login_required
def role_del(id):
    role=Role.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除角色:' + role.name + ',id:' + str(role.id))
        db.session.delete(role)
        flash('删除角色成功~','ok')
        return redirect(url_for('admin.role_list',page=1))
@app.route('/role/edit/<int:id>',methods=['GET','POST'])
@admin_login_required
def role_edit(id):
    role = Role.query.get_or_404(id)
    auth_list = request.values.getlist("auths")
    auth_list=list_to_str(auth_list)
    auth_dict = MultiDict([('auths', auth_list)])
    id_dict=MultiDict([('id',int(id))])
    values=CombinedMultiDict([auth_dict,request.form,id_dict])
    form = RoleEditForm(values)
    auths = Auth.query.all()
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            role.set_attr(form.data)
            db.session.add(role)
            Oplog('修改角色:' + role.name + ',id:' + str(role.id))
            flash('修改角色成功~','ok')
            return redirect(url_for('admin.role_edit',id=id))
    #修改ORM需要放在最后，否则其他数据库操作都不能执行，系统报错 unprintable InternalError object
    role.auths = str_to_list(role.auths)
    return render_template('admin/role_edit.html',form=form,auths=auths,role=role)

def list_to_str(data):
    auths = ','.join([str(v) for v in data])
    return auths

def str_to_list(data):
    auths = [int(v) for v in data.split(',')]
    return auths
