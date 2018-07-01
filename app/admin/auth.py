from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()

@app.route('/auth/add')
@admin_login_required
def auth_add():
    return render_template('admin/auth_add.html')
@app.route('/auth/list')
@admin_login_required
def auth_list():
    return render_template('admin/auth_list.html')
