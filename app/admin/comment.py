from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/comment/list')
@admin_login_required
def comment_list():
    return render_template('admin/comment_list.html')
