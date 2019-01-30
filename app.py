import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList,ItemIdList
from resources.home import Home, HomeList
from resources.describeItem import DescribeItem, DescribeItemList,DescribeItemIdList
from resources.describe import Describe, DescribeList
from resources.news import News
from resources.newstitle import NewsTitleList
from resources.newsbody import NewsBodyPlayUrl
app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Home, '/home/<string:name>')
api.add_resource(HomeList, '/homes')

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(ItemIdList, '/id_items/<int:homes_id>')

api.add_resource(Describe, '/describe/<string:name>')
api.add_resource(DescribeList, '/describes')


api.add_resource(DescribeItem, '/describeItem/<string:name>')
api.add_resource(DescribeItemList, '/describeItems')
api.add_resource(DescribeItemIdList, '/describeItemIdList/<int:describes_id>')

api.add_resource(UserRegister, '/register')

api.add_resource(News, '/news')
api.add_resource(NewsTitleList, '/newsTitle')
api.add_resource(NewsBodyPlayUrl, '/newsBody/<string:pageUrl>')

# api.add_resource(Translator, '/translator/<string:traText>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(host='0.0.0.0', port=5000)