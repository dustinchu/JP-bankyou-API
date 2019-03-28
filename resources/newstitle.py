from flask_restful import Resource, reqparse
from models.newstitle import NewsTtitleModel



#
# class NewsTitleList(Resource):
#     def get(self):
#         return list(map(lambda x: x.json(), NewsTtitleModel.query.all()))
class NewsTitleList(Resource):
    def get(self):
        return list(map(lambda x: x.json(), NewsTtitleModel.query.from_statement('select * from newstitle where date=(select max(date) from newstitle)')))
# rows = session.query(User).from_statement('SELECT * FROM user WHERE name=:name').params(name='user1')
#首先，query() 可以使用 from_statement() 方法，直接以完整的 SQL 指令進行查詢，更可以搭配 params() 將變數代入 SQL 指令中。