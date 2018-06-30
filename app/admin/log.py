from flask import render_template, redirect, url_for

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/log/oplog')
@admin_login_required
def oplog_list():
    return render_template('admin/oplog_list.html')
@app.route('/log/adminloginlog')
@admin_login_required
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')
@app.route('/log/userloginlog')
@admin_login_required
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')
