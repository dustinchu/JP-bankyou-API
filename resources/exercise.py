from flask_restful import Resource, reqparse
from models.exercise import ExerciseModel


class Exercise(Resource):
    parser = reqparse.RequestParser()


    def get(self, topic):
        exercise = ExerciseModel.find_by_name(topic)
        if exercise:
            return exercise.json()
        return {'message': 'exercise not found'}, 404

    def post(self, topic):
        print(topic)
        if ExerciseModel.find_by_name(topic):
            return {'message': "A exercise with name '{}' already exists.".format(topic)}, 400

        exercise = ExerciseModel(topic)
        try:
            exercise.save_to_db()
        except:
            return {"message": "An error occurred creating the exercise."}, 500

        return exercise.json(), 201

    def delete(self, topic):
        name = ExerciseModel.find_by_name(topic)
        if name:
            name.delete_from_db()

        return {'message': 'exercise deleted'}


class ExerciseList(Resource):
    def get(self):
        # return {StoreModel.query.all()}
        return list(map(lambda x: x.json(), ExerciseModel.query.all()))

