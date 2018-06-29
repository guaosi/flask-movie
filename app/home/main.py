from flask import render_template
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/')
def index():
    return render_template('home/index.html')
@app.route('/animation')
def animation():
    return render_template('home/animation.html')
@app.route('/search')
def search():
    return render_template('home/search.html')
@app.route('/play')
def play():
    return render_template('home/play.html')