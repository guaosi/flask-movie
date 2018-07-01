import datetime

from flask import render_template, request, flash, current_app, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.libs.upload import Upload_file
from app.models.movie import Movie
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
        upload=Upload_file()
        file_url=upload.video(form.url.data)
        file_logo=upload.video(form.logo.data)
        values=form.data
        values['url']=file_url
        values['logo']=file_logo
        values['playnum']=0
        values['commentnum']=0
        with db.auto_commit():
            movie=Movie()
            movie.set_attr(values)
            db.session.add(movie)
            flash('电影添加成功~','ok')
            return redirect(url_for('admin.movie_add'))
    return render_template('admin/movie_add.html',tags=tags,form=form)
@app.route('/movie/list')
@admin_login_required
def movie_list():
    return render_template('admin/movie_list.html')