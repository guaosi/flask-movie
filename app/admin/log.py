from flask import render_template, redirect, url_for
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/log/oplog')
def oplog_list():
    return render_template('admin/oplog_list.html')
@app.route('/log/adminloginlog')
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')
@app.route('/log/userloginlog')
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')
