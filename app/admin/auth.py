from flask import render_template

from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/pwd')
def pwd():
    return render_template('admin/pwd.html')
@app.route('/auth/add')
def auth_add():
    return render_template('admin/auth_add.html')
@app.route('/auth/list')
def auth_list():
    return render_template('admin/auth_list.html')
