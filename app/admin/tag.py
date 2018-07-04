from flask import render_template, request, flash, current_app, redirect, url_for

from app import db
from app.libs.login import admin_login_required,admin_auth
from app.libs.redprint import RedPrint
from app.models.oplog import Oplog
from app.models.tag import Tag
from app.validators.tag import TagForm

app=RedPrint()
@app.route('/tag/add',methods=['GET','POST'])
@admin_login_required
@admin_auth
def tag_add():
    form=TagForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            tag=Tag()
            tag.name=form.name.data
            db.session.add(tag)
            Oplog('添加标签:'+tag.name)
            flash('添加标签成功~','ok')
            return redirect(url_for('admin.tag_add'))
    return render_template('admin/tag_add.html',form=form)
@app.route('/tag/list/<int:page>')
@admin_login_required
@admin_auth
def tag_list(page=None):
    if page is None:
        page=1
    page_data= Tag.query.order_by(Tag.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_TAG_PAGE'])
    return render_template('admin/tag_list.html',page_data=page_data)

@app.route('/tag/del/<int:id>')
@admin_login_required
@admin_auth
def tag_del(id):
    tag=Tag.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除标签:' + tag.name + ',id:' + str(tag.id))
        db.session.delete(tag)
        flash('标签删除成功~','ok')
        return redirect(url_for('admin.tag_list',page=1))

@app.route('/tag/edit/<int:id>',methods=['GET','POST'])
@admin_login_required
@admin_auth
def tag_edit(id):
    tag=Tag.query.get_or_404(id)
    form=TagForm(request.form)
    if request.method=='POST' and form.validate():
        with db.auto_commit():
            tag.name=form.name.data
            db.session.add(tag)
            Oplog('修改标签:' + tag.name + ',id:' + str(tag.id))
            flash('标签修改成功~','ok')
            return redirect(url_for('admin.tag_edit'),id=id)
    return render_template('admin/tag_edit.html',form=form,tag=tag,id=id)
