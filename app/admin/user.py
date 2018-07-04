from flask import render_template, current_app, redirect, url_for, flash
from app import db
from app.libs.login import admin_login_required,admin_auth
from app.libs.redprint import RedPrint
from app.models.oplog import Oplog
from app.models.user import User
from app.models.userlog import Userlog
from app.models.moviecol import MovieCol
from app.models.comment import Comment
from app.models.movie import Movie


app=RedPrint()
@app.route('/user/list/<int:page>')
@admin_login_required
@admin_auth
def user_list(page=None):
    if page is None:
        page=1
    users=User.query.order_by(User.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_USER_PAGE'])
    return render_template('admin/user_list.html',users=users)
@app.route('/user/view/<int:id>')
@admin_login_required
def user_view(id):
    user=User.query.get_or_404(id)
    return render_template('admin/user_view.html',user=user)
@app.route('/user/del/<int:id>')
@admin_login_required
def user_del(id):
    user=User.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除用户:' + user.name + ',id:' + str(user.id))
        db.session.delete(user)
        flash('会员删除成功~','ok')
        return redirect(url_for('admin.user_list',page=1))

