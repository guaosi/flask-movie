from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/moviecol/list')
@admin_login_required
def moviecol_list():
    return render_template('admin/moviecol_list.html')
