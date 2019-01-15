from db import db


class NewsTtitleModel(db.Model):
    __tablename__ = 'newstitle'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    title = db.Column(db.String(300))
    img = db.Column(db.String(200))
    time = db.Column(db.String(50))
    url = db.Column(db.String(100))



    def __init__(self, date, title, img, time, url):
        self.date = date
        self.title = title
        self.img = img
        self.time = time
        self.url = url

    def json(self):
        return {'title': self.title, 'img': self.img, 'time': self.time, 'url': self.url}

    @classmethod
    def find_by_name(cls, title):
        return cls.query.filter_by(title=title).first()#return ItemModel object!


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
