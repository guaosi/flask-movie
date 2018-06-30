from flask import render_template
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/moviecol/list')
def moviecol_list():
    return render_template('admin/moviecol_list.html')
