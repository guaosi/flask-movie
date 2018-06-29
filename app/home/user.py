from flask import render_template
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/user')
def user():
    return render_template('home/user.html')
@app.route('/pwd')
def pwd():
    return render_template('home/pwd.html')
@app.route('/comments')
def comments():
    return render_template('home/comments.html')
@app.route('/loginlog')
def loginlog():
    return render_template('home/loginlog.html')
@app.route('/moviecol')
def moviecol():
    return render_template('home/moviecol.html')