from flask import render_template, current_app, flash, redirect, url_for

from app import db
from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.comment import Comment
from app.models.oplog import Oplog

app=RedPrint()
@app.route('/comment/list/<int:page>')
@admin_login_required
def comment_list(page=None):
    if page is None:
        page=1
    comments=Comment.query.order_by(Comment.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_COMMENT_PAGE'])
    return render_template('admin/comment_list.html',comments=comments)
@app.route('/comment/del/<int:id>')
@admin_login_required
def comment_del(id):
    comment=Comment.query.get_or_404(id)
    with db.auto_commit():
        Oplog('删除评论:' + comment.content + ',id:' + str(comment.id))
        db.session.delete(comment)
        flash('评论删除成功~','ok')
        return redirect(url_for('admin.comment_list',page=1))
