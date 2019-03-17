from db import db


class ExerciseItemModel(db.Model):
    __tablename__ = 'ExerciseItems'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    resultSelect = db.Column(db.String(150))
    answer = db.Column(db.String(100))

    exercises_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    exercise = db.relationship('ExerciseModel')

    def __init__(self, topic, resultSelect, answer, exercises_id):
        self.topic = topic
        self.resultSelect = resultSelect
        self.answer = answer
        self.exercises_id=exercises_id

    def json(self):
        return {'topic': self.topic, 'resultSelect': self.resultSelect,
                'answer': self.answer, 'exercises_id':self.exercises_id}

    @classmethod
    def find_by_name(cls, topic):
        return cls.query.filter_by(topic=topic).first()#return ItemModel object!

    @classmethod
    def find_by_id(cls, exercises_id):
        return cls.query.filter_by(exercises_id=exercises_id).first()  # return ItemModel object!

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
