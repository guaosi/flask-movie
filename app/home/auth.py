from flask import render_template, url_for, redirect
from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/login')
def login():
    return render_template('home/login.html')
@app.route('/logout')
def logout():
    return redirect(url_for('home.login'))
@app.route('/register')
def register():
    return render_template('home/register.html')