from flask_restful import Resource
from flask import request,session

from models import usermode
from exts import db

class register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = usermode.query.filter_by(username =username).first()
        if not user:
            newuser = usermode(username = username,password = password)
            db.session.add(newuser)
            db.session.commit()
            result ={
                "code":200,
                "message":"注册成功"
            }
        else:
            result={
                "code":500,
                "message":"该用户名已被注册"
            }
        return result

class login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = usermode.query.filter_by(username =username).first()
        if not user:
            result = {
                "code": 500,
                "message": "该用户名未被注册"
            }

        else:
            if password==user.password:
                session['username']=username
                result = {
                    "code": 200,
                    "message": "登录成功"
                }
            else:
                result = {
                    "code": 500,
                    "message": "密码错误"
                }
        return result