from flask import render_template

from app.libs.login import admin_login_required
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/movie/add')
@admin_login_required
def movie_add():
    return render_template('admin/movie_add.html')
@app.route('/movie/list')
@admin_login_required
def movie_list():
    return render_template('admin/movie_list.html')