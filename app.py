import os
from pathlib import Path
from flask import jsonify, request
from initializers import api, db, Resource, createApp
from models import certificates, course, course_videos, course_enrollment,students,quiz_questions,quiz_result
import parsers

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

app = createApp()
with app.app_context():
    db.init_app(app)
    api.init_app(app)
    db.create_all()

@api.route("/home")
class Home(Resource):
    def get(self):
        return jsonify({ "msg" : "Assalam O Alaikum"})


@api.route("/AddCourseInfo")
class CourseInfo(Resource):
    @api.expect(parsers.courseInfo)
    def post(self):
        try:
            

            title_ = request.form.get('title')
            description = request.form.get('description')
            language = request.form.get('language')
            introVideo = request.files.get('introVideo')
            poster = request.files.get('poster')

            s = r"D:\Pythonwork\TestEschool\static\courseIntoVid"
            path1 = os.path.join(s, introVideo.filename)
            introVideo.save(path1)

            d = r"D:\Pythonwork\TestEschool\static\coursePosters"
            path2= os.path.join(d, poster.filename)
            poster.save(path2)

            # ____________________________ Create Playlist as course name_____________________
            # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
            scopes1 = ["https://www.googleapis.com/auth/youtube.upload"]

            api_service_name = "youtube"
            api_version = "v3"
            client_secrets_file = "client_secrets_YT.json"

            # Get credentials and create an API client
            
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes1)
            credentials = flow.run_console()
            youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)



            requested = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "categoryId": "22",
                    "description": "Description of uploaded video.",
                    "title": title_
                },
                "status": {
                    "privacyStatus": "private"
                }
            },
            
            # TODO: For this request to work, you must replace "YOUR_FILE"
            #       with a pointer to the actual file you are uploading.
            media_body=MediaFileUpload(path1)
            )
            response = requested.execute()

            print(response)

            courseData = course.Courses(title = title_,
                                        description = description,
                                        language = language,
                                        introVideoLink = path1,
                                        posterLink = path2)
            # course.Courses.add_to_db(courseData)


            
            return jsonify({"msg":"Course Details are added"})
        except Exception as e:
            return jsonify({"msg":"Something went wrong" + str(e)})


@api.route("/AddCourseVideos")
class CourseInfo(Resource):
    @api.expect(parsers.courseInfo)
    def post(self):
        try:
            pass
        except Exception as e:
            pass


app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True)