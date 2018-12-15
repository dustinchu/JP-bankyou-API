from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
