from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.describeItem import DescribeItemModel


class DescribeItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('titleName',
                        type=str,
                        required=True,
                        help="titleName This field cannot be left blank!"
                        )
    parser.add_argument('titleBody',
                        type=str,
                        required=True,
                        help="titleBody This field cannot be left blank!"
                        )
    parser.add_argument('body',
                        type=str,
                        required=True,
                        help="body This field cannot be left blank!"
                        )
    parser.add_argument('exampleTitle',
                        type=str,
                        required=True,
                        help="exampleTitle This field cannot be left blank!"
                        )
    parser.add_argument('exampleBody',
                        type=str,
                        required=True,
                        help="exampleBody This field cannot be left blank!"
                        )

    parser.add_argument('describes_id',
                        type=int,
                        required=True,
                        help="Every item needs a describes_id."
                        )
    # 先把jwt認證關了
    # @jwt_required()
    def get(self, describes_id):
        item = DescribeItemModel.find_by_name(describes_id)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if DescribeItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = DescribeItem.parser.parse_args()

        item = DescribeItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = DescribeItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = DescribeItem.parser.parse_args()

        item = DescribeItemModel.find_by_name(name)

        if item:
            item.body = data['body']
        else:
            item = DescribeItemModel(name, **data)

        item.save_to_db()

        return item.json()


class DescribeItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), DescribeItemModel.query.all()))}

class DescribeItemIdList(Resource):

    def get(self, describes_id):
        return list(map(lambda x: x.json(), DescribeItemModel.query.filter_by(describes_id=describes_id)))