from flask import render_template, request, flash, current_app, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict, MultiDict

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.libs.upload import Upload_file
from app.models.movie import Movie
from app.validators.movie import MovieAddForm, MovieEditForm
from app.models.comment import Comment
from app.models.tag import Tag


app=RedPrint()
@app.route('/movie/add',methods=['GET','POST'])
@admin_login_required
def movie_add():
    # 将file跟form表单内容整合
    values = CombinedMultiDict([request.files, request.form])
    # id_dict=MultiDict([('id',10)])
    # values=CombinedMultiDict([id_dict,values])
    form=MovieAddForm(values)
    tags=Tag.query.all()
    if request.method=='POST' and form.validate():
        upload=Upload_file()
        file_url=upload.video(form.url.data)
        file_logo=upload.image(form.logo.data)
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
@app.route('/movie/list/<int:page>')
@admin_login_required
def movie_list(page=None):
    if page is None:
        page=1
    movies=Movie.query.order_by(Movie.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_MOVIE_PAGE'])
    return render_template('admin/movie_list.html',movies=movies)
@app.route('/movie/del/<int:id>')
@admin_login_required
def movie_del(id):
    movie=Movie.query.get_or_404(id)
    with db.auto_commit():
        db.session.delete(movie)
        flash('电影成功删除~','ok')
        return redirect(url_for('admin.movie_list',page=1))

@app.route('/movie/edit/<int:id>',methods=['GET','POST'])
@admin_login_required
def movie_edit(id):
    movie = Movie.query.get_or_404(id)
    # 将file跟form表单内容整合
    values = CombinedMultiDict([request.files, request.form])
    # 强行加入id，让方便验证器验证唯一性
    id_dict = MultiDict([('id',id)])
    values = CombinedMultiDict([id_dict,values])
    form = MovieEditForm(values)
    if request.method=='POST' and form.validate():
        if form.url.data != "":
            upload=Upload_file()
            movie.url=upload.video(form.url.data)
        if form.logo.data != "":
            upload = Upload_file()
            movie.logo = upload.video(form.logo.data)
        data = form.data
        # 存入url地址
        data['url']=movie.url
        data['logo']=movie.logo
        # 将不是手动录入字段先保存修改
        data['playnum']=movie.playnum
        data['commentnum']=movie.commentnum
        with db.auto_commit():
            # 一键修改属性
            movie.set_attr(data)
            db.session.add(movie)
            flash('电影修改成功~','ok')
            return redirect(url_for('admin.movie_edit',id=id))
    tags = Tag.query.all()
    return render_template('admin/movie_edit.html',movie=movie,tags=tags,form=form)
