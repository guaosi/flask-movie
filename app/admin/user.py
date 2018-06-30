from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/user/list')
@admin_login_required
def user_list():
    return render_template('admin/user_list.html')
@app.route('/user/view')
@admin_login_required
def user_view():
    return render_template('admin/user_view.html')
