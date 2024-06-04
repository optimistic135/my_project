from flask_restful import Resource
from flask import request,jsonify

import requests
import hashlib
import urllib.parse
import random
import re

def baidu_translate(word):
    for c in word:
        if 'a' <= c.lower() <= 'z':
            fromLang = 'en'
            toLang = 'zh'
        else:
            fromLang = 'zh'
            toLang = 'en'
    appid = '20231002001834745'
    secretKey = 'NDmPil5S5CJksfxKGZyr'
    q = word
    salt = random.randint(111, 999)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = f'http://fanyi-api.baidu.com/api/trans/vip/translate?q={urllib.parse.quote(q)}&from={fromLang}&to={toLang}&appid={appid}&salt={salt}&sign={sign}'
    try:
        res = requests.get(url).json()
        result = res['trans_result'][0]['dst']
        return result
    except Exception as e:
        print(e)

def is_english(s):
    return bool(re.search('[a-zA-Z]', s))

class translate(Resource):
    def post(self):
        data = request.get_json()
        word = data.get("word")
        if word:
            chinses = baidu_translate(word)
            if is_english(word):
                return jsonify({
                    "english": word,
                    "chinese": chinses
                })
            else:
                return jsonify({
                    "english": chinses,
                    "chinese": word
                })
        else:
            return jsonify({
                "english": None,
                "chinese": None
            })