from datetime import datetime
from typing import List
from initializers import db

class CourseVideos(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    courseId = db.Column(db.Integer, nullable = False)
    title = db.Column(db.String(128), unique = True, index = True)
    videoDesc = db.Column(db.String(128))
    videoLink = db.Column(db.String(128))
    viewCount = db.Column(db.Integer, nullable = False, default = 0)
    isDeleted = db.Column(db.Boolean(), default = False)
    deletedBy = db.Column(db.String(128))
    createdBy = db.Column(db.String(128))
    createdOn = db.Column(db.DateTime, default = datetime.now)
    
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id, isDeleted = False).first()

    @classmethod
    def find_by_courseId(cls, id):
        return cls.query.filter_by(courseId = id, isDeleted = False).first()

    @classmethod
    def getList(cls) -> List["CourseVideos"]:
        return cls.query.filter_by(isDeleted = False).all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()