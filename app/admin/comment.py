from flask import render_template
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/comment/list')
def comment_list():
    return render_template('admin/comment_list.html')
