from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    body = db.Column(db.String(80))

    homes_id = db.Column(db.Integer, db.ForeignKey('homes.id'))
    home = db.relationship('HomeModel')

    def __init__(self, name,  body, homes_id):
        self.name = name
        self.body = body
        self.homes_id = homes_id

    def json(self):
        return {'name': self.name, 'body': self.body, 'home_id': self.homes_id}

    @classmethod
    def find_by_name(cls, name):
        """
        cls.query.filter_by(name=name).first()
        select * from __tablename__ where name=name LIMIT 1
        .first()=return 1 row

        cls.query.filter_by(name=name).filter_by(id=id) or
        cls.query.filter_by(name=name, id=id)
        select * from __tablename__ where name=name  and id=id


        """
        return cls.query.filter_by(name=name).first()#return ItemModel object!

    @classmethod
    def find_by_id(cls, homes_id):
        return cls.query.filter_by(homes_id=homes_id).first()  # return ItemModel object!

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
