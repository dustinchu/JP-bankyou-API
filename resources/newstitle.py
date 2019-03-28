from flask_restful import Resource, reqparse
from models.newstitle import NewsTtitleModel



#
# class NewsTitleList(Resource):
#     def get(self):
#         return list(map(lambda x: x.json(), NewsTtitleModel.query.all()))
class NewsTitleList(Resource):
    def get(self):
        return list(map(lambda x: x.json(), NewsTtitleModel.query(NewsTtitleModel, max(NewsTtitleModel.date).over(partition_by=NewsTtitleModel.identifier, order_by=NewsTtitleModel.value))))
#