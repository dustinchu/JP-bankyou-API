from flask_restful import Resource, reqparse
from models.url import UrlModel


class Url(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('homeListViewUrl',
                        type=str,
                        required=True,
                        help="homeListViewUrl This field cannot be left blank!"
                        )
    parser.add_argument('courseListViewUrl',
                        type=str,
                        required=True,
                        help="courseListViewUrl This field cannot be left blank!"
                        )
    parser.add_argument('describeListViewUrl',
                        type=str,
                        required=True,
                        help="describeListViewUrl This field cannot be left blank!"
                        )
    parser.add_argument('describeItemListViewUrl',
                        type=str,
                        required=True,
                        help="describeItemListViewUrl This field cannot be left blank!"
                        )
    parser.add_argument('playUrl',
                        type=str,
                        required=True,
                        help="playUrl This field cannot be left blank!"
                        )

    parser.add_argument('newsTtile',
                        type=str,
                        required=True,
                        help="newsTtile item needs a describes_id."
                        )
    parser.add_argument('newsBody',
                        type=str,
                        required=True,
                        help="newsBody item needs a describes_id."
                        )
    parser.add_argument('exercise',
                        type=str,
                        required=True,
                        help="exercise item needs a describes_id."
                        )
    parser.add_argument('exerciseItem',
                        type=str,
                        required=True,
                        help="exerciseItem item needs a describes_id."
                        )


    def get(self, ver):
        ver = UrlModel.find_by_name(ver)
        if ver:
            return ver.json()
        return {'message': 'ver not found'}, 404

    def post(self, ver):
        if UrlModel.find_by_name(ver):
            return {'message': "A store with ver '{}' already exists.".format(UrlModel)}, 400

        data = Url.parser.parse_args()

        ver = UrlModel(ver, **data)
        # home = HomeModel(name, data['body'])
        try:
            ver.save_to_db()
        except:
            return {"message": "An error occurred creating the ver."}, 500

        return ver.json(), 201

    def delete(self, ver):
        ver = UrlModel.find_by_name(ver)
        if ver:
            ver.delete_from_db()

        return {'message': 'ver deleted'}


class UrlList(Resource):
    def get(self):
        # return {StoreModel.query.all()}
        return list(map(lambda x: x.json(), UrlModel.query.all()))

