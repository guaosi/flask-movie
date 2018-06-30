from flask import render_template

from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/admin/add')
def admin_add():
    return render_template('admin/admin_add.html')
@app.route('/admin/list')
def admin_list():
    return render_template('admin/admin_list.html')