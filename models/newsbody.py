from db import db


class NewsBodyModel(db.Model):
    __tablename__ = 'newsbody'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    pageUrl = db.Column(db.String(300))
    body = db.Column(db.String(200))
    playUrl = db.Column(db.String(50))



    def __init__(self, date, pageUrl, body, playUrl):
        self.date = date
        self.pageUrl = pageUrl
        self.body = body
        self.playUrl = playUrl

    def json(self):
        return {'pageUrl': self.pageUrl, 'body': self.body, 'playUrl': self.playUrl}

    @classmethod
    def find_by_name(cls, pageUrl):
        return cls.query.filter_by(pageUrl=pageUrl).first()#return ItemModel object!


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
