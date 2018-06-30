from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@admin_login_required
@app.route('/admin/add')
def admin_add():
    return render_template('admin/admin_add.html')
@app.route('/admin/list')
@admin_login_required
def admin_list():
    return render_template('admin/admin_list.html')