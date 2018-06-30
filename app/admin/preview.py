from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/preview/add')
@admin_login_required
def preview_add():
    return render_template('admin/preview_add.html')
@app.route('/preview/list')
@admin_login_required
def preview_list():
    return render_template('admin/preview_list.html')