from db import db


class DescribeItemModel(db.Model):
    __tablename__ = 'DescribeItems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    titleName = db.Column(db.String(150))
    titleBody = db.Column(db.String(150))
    body = db.Column(db.String(400))
    exampleTitle = db.Column(db.String(400))
    exampleBody = db.Column(db.String(400))

    describes_id = db.Column(db.Integer, db.ForeignKey('describes.id'))
    describe = db.relationship('DescribeModel')

    def __init__(self, name, titleName,titleBody, body,exampleTitle,exampleBody, describes_id):
        self.name = name
        self.titleName = titleName
        self.titleBody = titleBody
        self.exampleTitle = exampleTitle
        self.exampleBody = exampleBody
        self.body = body
        self.describes_id = describes_id

    def json(self):
        return {'name': self.name, 'titleName': self.titleName,
                'titleBody': self.titleBody, 'exampleTitle': self.exampleTitle,
                'exampleBody': self.exampleBody,
                'body': self.body, 'describes_id': self.describes_id}

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
    def find_by_id(cls, describes_id):
        return cls.query.filter_by(describes_id=describes_id).first()  # return ItemModel object!

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
