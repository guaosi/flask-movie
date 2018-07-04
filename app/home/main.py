import datetime
import uuid
from threading import Thread
from flask import render_template, request, current_app, flash, redirect, url_for, jsonify, Response
from flask_login import current_user, login_required
from app import db, rd, csrf
from app.libs.redprint import RedPrint
from app.models.comment import Comment
from app.models.movie import Movie
from app.models.moviecol import MovieCol
from app.models.preview import Preview
from app.models.tag import Tag
from app.validators.comment import CommentAddForm

app=RedPrint()
@app.route('/<int:page>/')
def index(page=None):
    if page is None:
        page=1
    tags=Tag.query.all()
    filter_condition=[]
    asc_condition=[]
    tid=int(request.args.get('tid','0'))
    if tid > 0:
        filter_condition.append(Movie.tag_id==tid)
    star=int(request.args.get('star','0'))
    if star > 0:
        filter_condition.append(Movie.star==star)
    time=int(request.args.get('time','0'))
    if time == 0:
        asc_condition.append(Movie.addtime.desc())
    pm=int(request.args.get('pm','0'))
    if pm == 0:
        asc_condition.append(Movie.playnum.desc())
    cm=int(request.args.get('cm','0'))
    if cm == 0:
        asc_condition.append(Movie.commentnum.desc())
    movies=Movie.query.filter(*filter_condition).order_by(*asc_condition).paginate(page=page,per_page=current_app.config['HOME_MOVIE_PAGE'])
    condition=dict(
        tid=tid,
        star=star,
        time=time,
        pm=pm,
        cm=cm
    )
    return render_template('home/index.html',tags=tags,condition=condition,movies=movies)
@app.route('/animation')
def animation():
    previews=Preview.query.all()
    return render_template('home/animation.html',previews=previews)
@app.route('/search/<int:page>')
def search(page=None):
    if page is None:
        page=1
    key=request.args.get('key','')
    movies=Movie.query.filter(Movie.title.like('%'+key+'%')).paginate(page,per_page=current_app.config['HOME_SEARCH_PAGE'])
    return render_template('home/search.html',movies=movies,key=key)
#普通逻辑
@app.route('/play/<int:id>/<int:page>',methods=['GET','POST'])
def play(id,page=None):
    movie=Movie.query.get_or_404(id)
    if page is None:
        page=1
    comments=Comment.query.filter_by(movie_id=id).order_by(Comment.addtime.desc()).paginate(page,per_page=current_app.config['HOME_COMMENT_PAGE'])
    app = current_app._get_current_object()
    thread=Thread(target=async_add_playnum,args=[id,app])
    thread.start()
    form = CommentAddForm(request.form)
    if request.method == 'POST' and form.validate():
        if not current_user.is_authenticated:
            return redirect(url_for('home.login'))
        value = form.data
        value['user_id'] = current_user.id
        comment = Comment()
        comment.set_attr(value)
        with db.auto_commit():
            db.session.add(comment)
        flash('添加评论成功~', 'ok')
        thread=Thread(target=async_add_commentnum,args=[form.movie_id.data,app])
        thread.start()
        return redirect(url_for('home.play', id=form.movie_id.data,page=page))
    return render_template('home/play.html',movie=movie,form=form,comments=comments)
# 弹幕逻辑
@app.route('/video/<int:id>/<int:page>',methods=['GET','POST'])
def video(id,page=None):
    movie=Movie.query.get_or_404(id)
    if page is None:
        page=1
    comments=Comment.query.filter_by(movie_id=id).order_by(Comment.addtime.desc()).paginate(page,per_page=current_app.config['HOME_COMMENT_PAGE'])
    app = current_app._get_current_object()
    thread=Thread(target=async_add_playnum,args=[id,app])
    thread.start()
    form = CommentAddForm(request.form)
    if request.method == 'POST' and form.validate():
        if not current_user.is_authenticated:
            return redirect(url_for('home.login'))
        value = form.data
        value['user_id'] = current_user.id
        comment = Comment()
        comment.set_attr(value)
        with db.auto_commit():
            db.session.add(comment)
        flash('添加评论成功~', 'ok')
        thread=Thread(target=async_add_commentnum,args=[form.movie_id.data,app])
        thread.start()
        return redirect(url_for('home.video', id=form.movie_id.data,page=page))
    return render_template('home/video.html',movie=movie,form=form,comments=comments)

@csrf.exempt
@app.route("/tm", methods=["GET", "POST"])
def tm():
    """
    弹幕消息处理
    """
    import json
    if request.method == "GET":
        # 获取弹幕消息队列
        id = request.args.get('id')
        # 存放在redis队列中的键值
        key = "movie" + str(id)
        if rd.llen(key):
            msgs = rd.lrange(key, 0, 2999)
            res = {
                "code": 1,
                "danmaku": [json.loads(v) for v in msgs]
            }
        else:
            res = {
                "code": 1,
                "danmaku": []
            }
        resp = json.dumps(res)
    if request.method == "POST":
        # 添加弹幕
        data = json.loads(request.get_data())
        msg = {
            "__v": 0,
            "author": data["author"],
            "time": data["time"],
            "text": data["text"],
            "color": data["color"],
            "type": data['type'],
            "ip": request.remote_addr,
            "_id": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex,
            "player": [
                data["player"]
            ]
        }
        res = {
            "code": 1,
            "data": msg
        }
        resp = json.dumps(res)
        # 将添加的弹幕推入redis的队列中
        rd.lpush("movie" + str(data["player"]), json.dumps(msg))
        print('发送')
    return Response(resp, mimetype='application/json')



# 异步任务
@app.route('/moviecol',methods=['POST'])
@login_required
def add_moviecol():
    data=request.form
    id=data['id']
    result=dict(data=1)
    movie=Movie.query.filter_by(id=id).first()
    if not movie:
        result['data']=-1
    moviecol_exists=MovieCol.query.filter_by(user_id=current_user.id,movie_id=id).first()
    if moviecol_exists:
        result['data']=0
    with db.auto_commit():
        moviecol=MovieCol()
        moviecol.user_id=current_user.id
        moviecol.movie_id=id
        db.session.add(moviecol)
    return jsonify(result)
def async_add_playnum(id,app):
    with app.app_context():
        try:
            movie = Movie.query.get_or_404(id)
            movie.playnum = movie.playnum + 1
            db.session.add(movie)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
def async_add_commentnum(id,app):
    with app.app_context():
        try:
            movie = Movie.query.get_or_404(id)
            movie.commentnum = movie.commentnum + 1
            db.session.add(movie)
            db.session.commit()
        except Exception as e:
            db.session.rollback()





