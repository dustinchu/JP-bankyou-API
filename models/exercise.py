from db import db


class ExerciseModel(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80))
    items = db.relationship('ExerciseItemModel', lazy='dynamic')

    def __init__(self, topic):
        self.topic = topic
        # self.body = body

    def json(self):
        # return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        return {'id': self.id, 'topic': self.topic}

    @classmethod
    def find_by_name(cls, topic):
        return cls.query.filter_by(topic=topic).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
