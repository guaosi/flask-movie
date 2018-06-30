from flask import render_template

from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/preview/add')
def preview_add():
    return render_template('admin/preview_add.html')
@app.route('/preview/list')
def preview_list():
    return render_template('admin/preview_list.html')