from flask_restful import Resource, reqparse
from models.newstitle import NewsTtitleModel




class NewsTitleList(Resource):
    def get(self):
        return list(map(lambda x: x.json(), NewsTtitleModel.query.all()))