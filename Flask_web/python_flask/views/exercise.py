from flask_restful import Resource
from flask import request,jsonify
import random

from models import words

class exer(Resource):
    def post(self):
        data = request.json
        num = int(data.get("num"))
        random_numbers = random.sample(range(1, 5557), num)
        result = []
        for id in random_numbers:
            exercise = words.query.filter_by(id=id).first()
            if exercise:
                result.append({
                    "id": exercise.id,
                    "english": exercise.English,
                    "chinese": exercise.Chinese,
                })
        return jsonify(result)

class judge(Resource):
    def post(self):
        data = request.json
        results = []

        for item in data:
            chinese = item.get("chinese")
            english = item.get("english")
            id = item.get("id")
            right = words.query.filter_by(id=id).first()
            if  english == right.English:
                results.append({"chinese": chinese, "english": right.English, "match": "√"})
            else:
                results.append({"chinese": chinese, "english": right.English, "match": "×"})

        return jsonify(results)

