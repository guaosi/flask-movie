from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/tag/add')
@admin_login_required
def tag_add():
    return render_template('admin/tag_add.html')
@app.route('/tag/list')
@admin_login_required
def tag_list():
    return render_template('admin/tag_list.html')
