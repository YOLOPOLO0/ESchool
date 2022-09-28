from datetime import datetime
from typing import List
from initializers import db

class QuizResult(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    courseId = db.Column(db.Integer, nullable = False)
    studentId = db.Column(db.Integer)
    quizId = db.Column(db.String(128))
    obtainMarks = db.Column(db.Integer)
    totalMarks = db.Column(db.Integer)
    createdOn = db.Column(db.DateTime, default = datetime.now)
    
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_courseId(cls, cid):
        return cls.query.filter_by(courseId = cid).first()

    @classmethod
    def find_by_quizId(cls, qid):
        return cls.query.filter_by(quizId = qid).first()

    @classmethod
    def getList(cls) -> List["QuizResult"]:
        return cls.query.all()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def commit():
        db.session.commit()