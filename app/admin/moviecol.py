from flask import render_template, current_app, redirect, url_for, flash

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.moviecol import MovieCol
from app.models.oplog import Oplog

app=RedPrint()
@app.route('/moviecol/list/<int:page>')
@admin_login_required
def moviecol_list(page=None):
    if page is None:
        page=1
    moviecols=MovieCol.query.order_by(MovieCol.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_MOVIECOL_PAGE'])
    return render_template('admin/moviecol_list.html',moviecols=moviecols)
@app.route('/moviecol/del/<int:id>')
@admin_login_required
def moviecol_del(id):
    moviecol=MovieCol.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除电影收藏:' + moviecol.movie.title + ',id:' + str(moviecol.id))
        db.session.delete(moviecol)
        flash('电影收藏删除成功~','ok')
        return redirect(url_for('admin.moviecol_list',page=1))
