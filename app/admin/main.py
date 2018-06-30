from flask import render_template, redirect, url_for

from app.libs.redprint import RedPrint
app=RedPrint()
@app.route('/')
def index():
    return render_template('admin/index.html')
@app.route('/login')
def login():
    return render_template('admin/login.html')
@app.route('/logout')
def logout():
    return redirect(url_for('admin.login'))
