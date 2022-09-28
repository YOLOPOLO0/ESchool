from datetime import datetime
from typing import List
from initializers import db

class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mainId = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    contactNo = db.Column(db.String(80))
    roleId = db.Column(db.String(80))
    DPurl = db.Column(db.String(80))
    DPthumbnail = db.Column(db.String(80))
    createdOn = db.Column(db.DateTime, default = datetime.now)


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_mainId(cls, _id):
        return cls.query.filter_by(mainId = _id).first()

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(name = _name).first()

    @classmethod
    def getList(cls) -> List["StudentModel"]:
        return cls.query.all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()

    