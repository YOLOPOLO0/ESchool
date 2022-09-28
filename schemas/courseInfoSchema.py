from initializers import ma
from models.course import Courses


class CourseInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Courses
        load_instance = True
        include_fk= True