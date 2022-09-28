from datetime import datetime
from typing import List
from initializers import db

class CourseEnrollment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    courseId = db.Column(db.Integer, nullable = False)
    studentId = db.Column(db.Integer)
    status = db.Column(db.String(64))
    createdOn = db.Column(db.DateTime, default = datetime.now)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def getList(cls) -> List["CourseEnrollment"]:
        return cls.query.all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()