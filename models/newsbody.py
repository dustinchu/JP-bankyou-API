from db import db


class NewsBodyModel(db.Model):
    __tablename__ = 'newsbody'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    pageurl = db.Column(db.String(300))
    body = db.Column(db.String(200))
    playurl = db.Column(db.String(50))



    def __init__(self, date, pageurl, body, playurl):
        self.date = date
        self.pageurl = pageurl
        self.body = body
        self.playurl = playurl

    def json(self):
        return {'pageurl': self.pageurl, 'body': self.body, 'playurl': self.playurl}

    @classmethod
    def find_by_name(cls, pageurl):
        return cls.query.filter_by(pageurl=pageurl).first()#return ItemModel object!


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
