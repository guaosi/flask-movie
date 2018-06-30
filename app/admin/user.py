from flask import render_template
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/user/list')
def user_list():
    return render_template('admin/user_list.html')
@app.route('/user/view')
def user_view():
    return render_template('admin/user_view.html')
