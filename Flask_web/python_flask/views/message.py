from flask_restful import Resource
from flask import request,jsonify

from models import learning
from exts import db

class addword(Resource):
    def post(self):
        data = request.json
        word = data.get("word")
        chinese = data.get("chinese")
        username = data.get("username")
        add = learning(username = username,English = word,Chinese = chinese)
        isalready = learning.query.filter_by(English = word).all()
        allname = [learning.username for learning in isalready]
        if username in allname:
            result={
                "code":"500",
                "message":"您已经添加"
            }
        else:
            db.session.add(add)
            db.session.commit()
            result = {
                "code": "500",
                "message": "添加成功"
            }
        return result


class mes(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        msger = learning.query.filter_by(username = username).all()
        result = []
        for user in msger:
            result.append({
                "english":user.English,
                "chinese":user.Chinese,
                "join_time":user.join_time
            })
        return jsonify(result)

class deleteword(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        word = data.get("English")
        msg = learning.query.filter_by(username = username,English = word).all()
        if msg:
            for m in msg:
                db.session.delete(m)
            db.session.commit()
            result = {
                "code": "200",
                "message": "sucessful!"
            }
        else:
            result = {
                "code": "500",
                "message": "单词不存在"
            }
        return jsonify(result)