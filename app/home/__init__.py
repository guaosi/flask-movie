from flask import Blueprint, render_template
from app.home import auth,main,user
bp = Blueprint('home',__name__)
def create_home_blueprint():
    auth.app.register(bp)
    main.app.register(bp)
    user.app.register(bp)
    return bp
@bp.app_errorhandler(404)
def not_found(e):
    return render_template('common/404.html')