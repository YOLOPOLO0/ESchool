from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage

courseInfo = reqparse.RequestParser(bundle_errors=False)

courseInfo.add_argument(name = 'title',
                        type = str,
                        location = 'form',
                        required = True,
                        help = "Title of Course")

courseInfo.add_argument(name = 'description',
                        type = str,
                        location = 'form',
                        required = True,
                        help = "Description of Course")

courseInfo.add_argument(name = 'language',
                        type = str,
                        location = 'form',
                        required = True,
                        help = "medium/language of Course")


courseInfo.add_argument(name = 'introVideo',
                        type = FileStorage,
                        location = 'files',
                        help = "Intro Video of Course")

