from threading import Thread

from flask import render_template, request, flash, redirect, url_for, current_app
from werkzeug.datastructures import CombinedMultiDict

from app import db
from app.libs.redprint import RedPrint
from flask_login import login_required, current_user

from app.libs.upload import Upload_file
from app.models.comment import Comment
from app.models.movie import Movie
from app.models.moviecol import MovieCol
from app.models.userlog import Userlog
from app.validators.comment import CommentAddForm
from app.validators.user import UserEditForm, UserPwdForm

app=RedPrint()
@app.route('/user',methods=['GET','POST'])
@login_required
def user():
    user=current_user
    values = CombinedMultiDict([request.files, request.form])
    form=UserEditForm(values)
    if request.method=='POST' and form.validate():
        data = form.datadata=form.data
        if form.face.data != "":
            upload=Upload_file()
            user.face=upload.image(form.face.data)
        data['face'] = user.face
        user.set_attr(data)
        with db.auto_commit():
            db.session.add(user)
        flash('修改会员资料成功~','ok')
        return redirect(url_for('home.user'))
    return render_template('home/user.html',user=user,form=form)
@app.route('/pwd',methods=['GET','POST'])
@login_required
def pwd():
    form=UserPwdForm(request.form)
    if request.method=='POST' and form.validate():
        user=current_user._get_current_object()
        with db.auto_commit():
            user.pwd=form.newpwd.data
            db.session.add(user)
        flash('密码修改成功,请重新登陆~','ok')
        return redirect(url_for('home.logout'))
    return render_template('home/pwd.html',form=form)
@app.route('/comments/<int:page>')
@login_required
def comments(page=None):
    if page is None:
        page=1
    comments=Comment.query.filter_by(user_id=current_user.id).order_by(Comment.addtime.desc()).paginate(page,per_page=current_app.config['HOME_COMMENT_PAGE'])
    return render_template('home/comments.html',comments=comments)
@app.route('/loginlog/<int:page>')
@login_required
def loginlog(page=None):
    if page is None:
        page = 1
    loginlogs = Userlog.query.filter_by(user_id=current_user.id).order_by(Userlog.addtime.desc()).paginate(page, per_page=current_app.config['ADMIN_USERLOGINLOG_PAGE'])
    return render_template('home/loginlog.html',loginlogs=loginlogs)
@app.route('/moviecol/<int:page>')
@login_required
def moviecol(page=None):
    moviecols=MovieCol.query.filter_by(user_id=current_user.id).order_by(MovieCol.addtime.desc()).paginate(page,per_page=current_app.config['HOME_MOVIECOL_PAGE'])
    return render_template('home/moviecol.html',moviecols=moviecols)