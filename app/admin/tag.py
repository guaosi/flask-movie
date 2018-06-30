from flask import render_template
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/tag/add')
def tag_add():
    return render_template('admin/tag_add.html')
@app.route('/tag/list')
def tag_list():
    return render_template('admin/tag_list.html')
