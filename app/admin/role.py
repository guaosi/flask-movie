from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/role/add')
@admin_login_required
def role_add():
    return render_template('admin/role_add.html')
@app.route('/role/list')
@admin_login_required
def role_list():
    return render_template('admin/role_list.html')