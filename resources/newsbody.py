from flask_restful import Resource, reqparse
from models.newsbody import NewsBodyPlayUrlModel




class NewsBodyPlayUrl(Resource):
    def get(self, pageUrl):
        print(pageUrl)
        return NewsBodyPlayUrlModel.getPlayUrl(pageUrl)