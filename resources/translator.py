from flask_restful import Resource, reqparse

import nagisa

class Translator(Resource):
    def get(self, traText):
        text = '(๑¯ω¯๑)Pythonで簡単に使えるツールです'
        # output = 'Python/名詞 で/助詞 簡単/形状詞 に/助動詞 使える/動詞 ツール/名詞 です/助動詞'
        words = nagisa.tagging(text)
        return str(words)