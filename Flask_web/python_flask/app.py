from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from flask_migrate import Migrate

from exts import db,cors
import config

from views.translate import translate
from views.auth import register,login
from views.message import addword,mes,deleteword
from views.exercise import exer,judge

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app,db)

api = Api(app)
cors.init_app(app)


class nihaoapi(Resource):
    def get(self):
        data =  [
            {
                "english": "xu",
                "chinese": 18,
                "join_time": "man"
            },
            {
                "english": "lll",
                "chinese":20,
                "join_time": "woman"
            }
    ]
        return data
    def post(self):
        data = request.get_json()
        username = data.get('username')
        res = f"post form {username}"
        return jsonify({"message":res})

api.add_resource(nihaoapi,"/nihaoapi")

api.add_resource(translate,"/translate")
api.add_resource(register,"/register")
api.add_resource(login,"/login")
api.add_resource(addword,"/addword")
api.add_resource(mes,"/mes")
api.add_resource(deleteword,"/detele")
api.add_resource(exer,"/exer")
api.add_resource(judge,"/judge")

if __name__ == '__main__':
    app.run()
