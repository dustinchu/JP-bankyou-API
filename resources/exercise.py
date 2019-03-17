from flask_restful import Resource, reqparse
from models.exercise import ExerciseModel


class Exercise(Resource):
    parser = reqparse.RequestParser()


    def get(self, name):
        exercise = ExerciseModel.find_by_name(name)
        if exercise:
            return exercise.json()
        return {'message': 'exercise not found'}, 404

    def post(self, name):
        if ExerciseModel.find_by_name(name):
            return {'message': "A exercise with name '{}' already exists.".format(name)}, 400

        # home = HomeModel(name, data['body'])
        exercise = ExerciseModel(name)
        try:
            exercise.save_to_db()
        except:
            return {"message": "An error occurred creating the exercise."}, 500

        return exercise.json(), 201

    def delete(self, name):
        name = ExerciseModel.find_by_name(name)
        if name:
            name.delete_from_db()

        return {'message': 'exercise deleted'}


class ExerciseList(Resource):
    def get(self):
        # return {StoreModel.query.all()}
        return list(map(lambda x: x.json(), ExerciseModel.query.all()))

