from flask import render_template, request, flash
from werkzeug.datastructures import CombinedMultiDict

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.validators.movie import MovieAddForm
from app.models.comment import Comment
from app.models.tag import Tag


app=RedPrint()
@app.route('/movie/add',methods=['GET','POST'])
@admin_login_required
def movie_add():
    values = CombinedMultiDict([request.files, request.form])
    form=MovieAddForm(values)
    tags=Tag.query.all()
    if request.method=='POST' and form.validate():
        flash('电影添加成功~','ok')
    return render_template('admin/movie_add.html',tags=tags,form=form)
@app.route('/movie/list')
@admin_login_required
def movie_list():
    return render_template('admin/movie_list.html')