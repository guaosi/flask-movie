from flask import render_template

from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/movie/add')
def movie_add():
    return render_template('admin/movie_add.html')
@app.route('/movie/list')
def movie_list():
    return render_template('admin/movie_list.html')