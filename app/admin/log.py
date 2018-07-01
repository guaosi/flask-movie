from flask import render_template, redirect, url_for, current_app

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
from app.models.adminlog import Adminlog
from app.models.oplog import Oplog
from app.models.userlog import Userlog

app=RedPrint()
@app.route('/log/oplog/<int:page>')
@admin_login_required
def oplog_list(page=None):
    if page is None:
        page=1
    oplogs=Oplog.query.order_by(Oplog.addtime.desc()).paginate(page,per_page=current_app.config['ADMIN_OPLOG_PAGE'])
    return render_template('admin/oplog_list.html',oplogs=oplogs)
@app.route('/log/adminloginlog/<int:page>')
@admin_login_required
def adminloginlog_list(page=None):
    if page is None:
        page = 1
    adminloginlogs =Adminlog.query.order_by(Adminlog.addtime.desc()).paginate(page, per_page=current_app.config['ADMIN_ADMINLOGINLOG_PAGE'])
    return render_template('admin/adminloginlog_list.html',adminloginlogs=adminloginlogs)
@app.route('/log/userloginlog/<int:page>')
@admin_login_required
def userloginlog_list(page=None):
    if page is None:
        page = 1
    userloginlogs = Userlog.query.order_by(Userlog.addtime.desc()).paginate(page, per_page=current_app.config['ADMIN_USERLOGINLOG_PAGE'])
    return render_template('admin/userloginlog_list.html',userloginlogs=userloginlogs)
