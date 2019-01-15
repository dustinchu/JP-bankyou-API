from flask_restful import Resource, reqparse
from models.newsbody import NewsBodyModel




class NewsBodyList(Resource):
    def get(self):
        return list(map(lambda x: x.json(), NewsBodyModel.query.all()))