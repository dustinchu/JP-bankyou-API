from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('type',
                        type=str,
                        required=True,
                        help="Every item needs a type."
                        )
    parser.add_argument('body',
                        type=str,
                        required=True,
                        help="Every item needs a body."
                        )
    parser.add_argument('exampleTitle',
                        type=str,
                        required=True,
                        help="Every item needs a exampleTitle."
                        )
    parser.add_argument('exampleBody',
                        type=str,
                        required=True,
                        help="Every item needs a exampleBody."
                        )
    parser.add_argument('homes_id',
                        type=int,
                        required=True,
                        help="Every item needs a homes_id."
                        )

    # 先把jwt認證關了
    # @jwt_required()
    def get(self, title):
        item = ItemModel.find_by_name(title)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, title):

        if ItemModel.find_by_name(title):
            return {'message': "An item with title '{}' already exists.".format(title)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(title, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.body = data['body']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

class ItemIdList(Resource):

    def get(self, homes_id):
        return list(map(lambda x: x.json(), ItemModel.query.filter_by(homes_id=homes_id)))