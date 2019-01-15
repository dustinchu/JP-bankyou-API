from flask_restful import Resource, reqparse
from models.newsbody import NewsBody




class NewsBody(Resource):
    def get(self):
        return list(map(lambda x: x.json(), NewsBody.query.all()))