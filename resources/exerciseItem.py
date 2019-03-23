from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.exerciseItem import ExerciseItemModel


class ExerciseItem(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('resultSelect',
                        type=str,
                        required=True,
                        help="resultSelect This field cannot be left blank!"
                        )
    parser.add_argument('answer',
                        type=int,
                        required=True,
                        help="answer This field cannot be left blank!"
                        )
    parser.add_argument('exercises_id',
                        type=int,
                        required=True,
                        help="Every item needs a exercises_id."
                        )
    # 先把jwt認證關了
    # @jwt_required()
    def get(self, exercise_id):
        item = ExerciseItemModel.find_by_id(exercise_id)
        if item:
            return item.json()
        return {'message': 'ExerciseItem not found'}, 404

    def post(self, topic):
        if ExerciseItemModel.find_by_name(topic):
            return {'message': "An item with topic '{}' already exists.".format(topic)}, 400

        data = ExerciseItem.parser.parse_args()

        item = ExerciseItemModel(topic, **data)
        # print(item.json())
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the ExerciseItem."}, 500

        return item.json(), 201

    def delete(self, topic):
        item = ExerciseItemModel.find_by_name(topic)
        if item:
            item.delete_from_db()
            return {'message': 'ExerciseItem deleted.'}
        return {'message': 'ExerciseItem not found.'}, 404

    def put(self, topic):
        data = ExerciseItem.parser.parse_args()

        item = ExerciseItemModel.find_by_name(topic)

        if item:
            item.body = data['resultSelect']
        else:
            item = ExerciseItemModel(topic, **data)

        item.save_to_db()

        return item.json()


class ExerciseItemList(Resource):
    def get(self):
        return {'ExerciseItem': list(map(lambda x: x.json(), ExerciseItemModel.query.all()))}

class ExerciseItemIdList(Resource):

    def get(self, exercises_id):
        return list(map(lambda x: x.json(), ExerciseItemModel.query.filter_by(exercises_id=exercises_id)))