from flask import Blueprint
from app.home import test
def create_home_blueprint():
    bp = Blueprint('home',__name__)
    test.app.register(bp)
    return bp