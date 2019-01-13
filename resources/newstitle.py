from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.newstitle import NewsTtitleModel




class NewsTitleList(Resource):
    def get(self):
        return {'NewsTitleList': list(map(lambda x: x.json(), NewsTtitleModel.query.all()))}