from datetime import datetime
from typing import List
from initializers import db


class Courses(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    playlistId = db.Column(db.String(128))
    coursePlaylistLink = db.Column(db.String(128))
    title = db.Column(db.String(128), nullable = False, unique = True, index = True)
    description = db.Column(db.String(128), nullable  = False)
    language = db.Column(db.String(128), nullable = False)
    duration = db.Column(db.String(64), default = 0)
    enrollments = db.Column(db.Integer, nullable = False, default = 0)
    introVideoLink = db.Column(db.String(128))
    IntroThumbnailLink = db.Column(db.String(128))
    isDeleted = db.Column(db.Boolean(), default = False)
    deletedBy = db.Column(db.String(128))
    createdOn = db.Column(db.DateTime, default = datetime.now)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id, isDeleted = False).first()

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(title = _name, isDeleted = False).first()

    @classmethod
    def getList(cls) -> List["Courses"]:
        return cls.query.filter_by(isDeleted = False).all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()