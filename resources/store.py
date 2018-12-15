from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):




    def get(self, title):
        store = StoreModel.find_by_name(title)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, title):
        if StoreModel.find_by_name(title):
            return {'message': "A store with name '{}' already exists.".format(title)}, 400

        store = StoreModel(title)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, title):
        store = StoreModel.find_by_name(title)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        # return {StoreModel.query.all()}
        return {'1': list(map(lambda x: x.json(), StoreModel.query.all()))}

