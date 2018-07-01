import datetime
from flask import Blueprint
from app.admin import main,auth,tag,preview,movie,user,moviecol,comment,log,admin,role
bp=Blueprint('admin',__name__)
@bp.context_processor
def tel_extra():
    data=dict(
        online_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    return data
def create_admin_blueprint():
    main.app.register(bp,url_prefix='/admin')
    auth.app.register(bp,url_prefix='/admin')
    tag.app.register(bp,url_prefix='/admin')
    movie.app.register(bp,url_prefix='/admin')
    preview.app.register(bp,url_prefix='/admin')
    user.app.register(bp,url_prefix='/admin')
    comment.app.register(bp,url_prefix='/admin')
    moviecol.app.register(bp,url_prefix='/admin')
    log.app.register(bp,url_prefix='/admin')
    admin.app.register(bp,url_prefix='/admin')
    role.app.register(bp,url_prefix='/admin')
    return bp
