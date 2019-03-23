from db import db


class UrlModel(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    ver = db.Column(db.String(80))
    homeListViewUrl = db.Column(db.String(150))
    courseListViewUrl = db.Column(db.String(150))
    describeListViewUrl = db.Column(db.String(150))
    describeItemListViewUrl = db.Column(db.String(150))
    playUrl = db.Column(db.String(150))
    newsTtile = db.Column(db.String(150))
    newsBody = db.Column(db.String(150))
    exercise = db.Column(db.String(150))
    exerciseItem = db.Column(db.String(150))

    def __init__(self, ver, homeListViewUrl, courseListViewUrl, describeListViewUrl, describeItemListViewUrl, playUrl, newsTtile, newsBody, exercise, exerciseItem):
        self.ver = ver
        self.homeListViewUrl = homeListViewUrl
        self.courseListViewUrl = courseListViewUrl
        self.describeListViewUrl = describeListViewUrl
        self.describeItemListViewUrl = describeItemListViewUrl
        self.playUrl = playUrl
        self.newsTtile = newsTtile
        self.newsBody = newsBody
        self.exercise = exercise
        self.exerciseItem = exerciseItem

        # self.body = body

    def json(self):
        # return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        return {'id': self.id, 'ver': self.ver, 'homeListViewUrl': self.homeListViewUrl, 'courseListViewUrl': self.courseListViewUrl,
                'describeListViewUrl': self.describeListViewUrl, 'describeItemListViewUrl': self.describeItemListViewUrl,
                'playUrl': self.playUrl, 'newsTtile': self.newsTtile, 'newsBody': self.newsBody, 'exercise': self.exercise,
                'exerciseItem': self.exerciseItem}

    @classmethod
    def find_by_name(cls, ver):
        return cls.query.filter_by(ver=ver).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
