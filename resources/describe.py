from flask_restful import Resource, reqparse
from models.describe import DescribeModel


class Describe(Resource):
    parser = reqparse.RequestParser()


    def get(self, name):
        home = DescribeModel.find_by_name(name)
        if home:
            return home.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if DescribeModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        # home = HomeModel(name, data['body'])
        home = DescribeModel(name)
        try:
            home.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return home.json(), 201

    def delete(self, home):
        home = DescribeModel.find_by_name(home)
        if home:
            home.delete_from_db()

        return {'message': 'Store deleted'}


class DescribeList(Resource):
    def get(self):
        # return {StoreModel.query.all()}
        return list(map(lambda x: x.json(), DescribeModel.query.all()))

