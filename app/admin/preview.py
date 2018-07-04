from flask import render_template, request, flash, redirect, url_for, current_app
from werkzeug.datastructures import CombinedMultiDict, MultiDict

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.libs.upload import Upload_file
from app.models.oplog import Oplog
from app.models.preview import Preview
from app.validators.preview import PreviewAddForm, PreviewEditForm

app=RedPrint()
@app.route('/preview/add',methods=['GET','POST'])
@admin_login_required
def preview_add():
    values=CombinedMultiDict([request.files,request.form])
    form=PreviewAddForm(values)
    if request.method=='POST' and form.validate():
        upload=Upload_file()
        logo=upload.image(form.logo.data)
        data = form.data
        data['logo']=logo
        with db.auto_commit():
            preview=Preview()
            preview.set_attr(data)
            db.session.add(preview)
            Oplog('添加预告:' + preview.title)
            flash('预告添加成功~','ok')
            return redirect(url_for('admin.preview_add'))
    return render_template('admin/preview_add.html',form=form)
@app.route('/preview/list/<int:page>')
@admin_login_required
def preview_list(page=None):
    if page is None:
        page=1
    previews=Preview.query.order_by(Preview.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_PREVIEW_PAGE'])
    return render_template('admin/preview_list.html',previews=previews)

@app.route('/preview/del/<int:id>')
@admin_login_required
def preview_del(id):
    preview=Preview.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除预告:' + preview.title + ',id:' + str(preview.id))
        db.session.delete(preview)
        flash('预告删除成功~','ok')
        return redirect(url_for('admin.preview_list',page=1))

@app.route('/preview/edit/<int:id>',methods=['GET','POST'])
@admin_login_required
def preview_edit(id):
    preview=Preview.query.get_or_404(id)
    values = CombinedMultiDict([request.files, request.form])
    id_dict=MultiDict([('id',id)])
    values=CombinedMultiDict([values,id_dict])
    form = PreviewEditForm(values)
    if request.method=='POST' and form.validate():
        if form.logo.data != '':
            upload=Upload_file()
            preview.logo=upload.image(form.logo.data)
        data=form.data
        data['logo']=preview.logo
        with db.auto_commit():
            preview.set_attr(data)
            db.session.add(preview)
            Oplog('修改预告:' + preview.title + ',id:' + str(preview.id))
            flash('预告修改成功~','ok')
            return redirect(url_for('admin.preview_edit',id=id))
    return render_template('admin/preview_edit.html',preview=preview,form=form)