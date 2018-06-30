from flask import render_template

from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/role/add')
def role_add():
    return render_template('admin/role_add.html')
@app.route('/role/list')
def role_list():
    return render_template('admin/role_list.html')