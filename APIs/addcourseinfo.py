from flask_restplus import Resource, Namespace
from initializers import YOUTUBE_PLAYLIST_URL_PREFIX, YOUTUBE_VIDEO_URL_PREFIX, createPlaylist, uploadIntroVideo
from models.course import Courses
from parsers import courseInfo
from flask import request, jsonify
import os


courseInfo_ns = Namespace('CourseInfo', description= 'ADD Course INFO')


@courseInfo_ns.route("/AddCourseInfo")
class CourseInfo(Resource):
    @courseInfo_ns.expect(courseInfo)
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

            playlistId = createPlaylist(title_, description)
            introVideoResponse = uploadIntroVideo(path1, title_, description)


            courseData = Courses(playlistId = playlistId,
                                coursePlaylistLink = YOUTUBE_PLAYLIST_URL_PREFIX + playlistId,
                                title = title_,
                                description = description,
                                language = language,
                                introVideoLink = YOUTUBE_VIDEO_URL_PREFIX + introVideoResponse['id'],
                                IntroThumbnailLink = introVideoResponse['snippet']['thumbnails']['high']['url'])
            Courses.add_to_db(courseData)

            return jsonify({"msg":"Course Details are added"})

        except Exception as e:
            return jsonify({"msg":"Something went wrong" + str(e)})