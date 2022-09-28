from datetime import datetime
from typing import List
from initializers import db

class QuizQuestions(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    courseId = db.Column(db.Integer, nullable = False)
    Qno = db.Column(db.Integer)
    question = db.Column(db.String())
    option1 = db.Column(db.String())
    Option2 = db.Column(db.String())
    option3 = db.Column(db.String())
    option4 = db.Column(db.String())
    correntAnswer = db.Column(db.String())
    isDeleted = db.Column(db.Boolean(), default = False)
    deletedBy = db.Column(db.String(128))
    createdBy = db.Column(db.String(128)) 
    createdOn = db.Column(db.DateTime, default = datetime.now)
    
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id, isDeleted = False).first()

    @classmethod
    def find_by_Qno(cls, _name):
        return cls.query.filter_by(Qno = _name, isDeleted = False).first()

    @classmethod
    def getList(cls) -> List["QuizQuestions"]:
        return cls.query.filter_by(isDeleted = False).all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()