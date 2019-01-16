from db import db


class NewsBodyModel(db.Model):
    __tablename__ = 'newsbody'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    url = db.Column(db.String(300))
    body = db.Column(db.String(900))
    music = db.Column(db.String(100))



    def __init__(self, date, url, body, music):
        self.date = date
        self.url = url
        self.body = body
        self.music = music

    def json(self):
        return {'url': self.url, 'body': self.body, 'music': self.music}

    @classmethod
    def find_by_name(cls, url):
        return cls.query.filter_by(url=url).first()#return ItemModel object!


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
