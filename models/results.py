from datetime import datetime
from typing import List
from initializers import db

class Results(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    courseId = db.Column(db.Integer, nullable = False)
    studentId = db.Column(db.String(128))
    obtainedPercentage = db.Column(db.String(128))
    createdOn = db.Column(db.DateTime, default = datetime.now)
    
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id, isDeleted = False).first()

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(name = _name, isDeleted = False).first()

    @classmethod
    def getList(cls) -> List["Results"]:
        return cls.query.filter_by(isDeleted = False).all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()