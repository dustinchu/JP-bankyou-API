from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(80))
    type = db.Column(db.String(20))
    body = db.Column(db.String(80))
    exampleTitle = db.Column(db.String(150))
    exampleBody = db.Column(db.String(150))

    homes_id = db.Column(db.Integer, db.ForeignKey('homes.id'))
    home = db.relationship('HomeModel')

    def __init__(self, title,  type, body, exampleTitle, exampleBody, homes_id):
        self.title = title
        self.type = type
        self.body = body
        self.exampleTitle = exampleTitle
        self.exampleBody = exampleBody
        self.homes_id = homes_id


    def json(self):
        return {'title': self.title, 'type': self.type, 'body': self.body,
                'exampleTitle': self.exampleTitle, 'exampleBody': self.exampleBody, 'homes_id': self.homes_id}

    @classmethod
    def find_by_name(cls, title):
        """
        cls.query.filter_by(name=name).first()
        select * from __tablename__ where name=name LIMIT 1
        .first()=return 1 row

        cls.query.filter_by(name=name).filter_by(id=id) or
        cls.query.filter_by(name=name, id=id)
        select * from __tablename__ where name=name  and id=id


        """
        return cls.query.filter_by(title=title).first()#return ItemModel object!

    @classmethod
    def find_by_id(cls, homes_id):
        return cls.query.filter_by(homes_id=homes_id).first()  # return ItemModel object!

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
