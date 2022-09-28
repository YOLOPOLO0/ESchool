import os
from flask import Flask
from flask_restplus import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import google_auth_oauthlib
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload

def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

db = SQLAlchemy()
api = Api()

API_KEY = "AIzaSyBhEZAQC2ZCMIarOy1Z-u5SkmP9wjdxCC8"
YOUTUBE_PLAYLIST_URL_PREFIX = "https://www.youtube.com/playlist?list=" #contatenate playlist id
YOUTUBE_VIDEO_URL_PREFIX = "https://youtu.be/" #concatenate video id


Resource = Resource


def getAuthenticated():
    credentialPath = os.path.abspath('credentials.json')
    store = os.storage()


def createPlaylist(title_, description):
    scopes = ["https://www.googleapis.com/auth/youtubepartner"]

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets_YT.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    requested = youtube.playlists().insert(
                                            part="snippet,status",
                                            body={
                                                    "snippet": {
                                                                    "title": title_,
                                                                    "description": description,
                                                                    "tags": [
                                                                                title_,
                                                                                "course"
                                                                            ],
                                                                    "defaultLanguage": "en"
                                                                },
                                                    "status": {
                                                                    "privacyStatus": "public"
                                                                }
                                                }
                                        )

    response = requested.execute()
    print(response)
    return response['id']

def uploadIntroVideo(path1, title_, description):
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
                                                "description": description,
                                                "title": title_
                                            },
                                            "status": {
                                                "privacyStatus": "private"
                                            }
                                        },
                                        
                                        # TODO: For this request to work, you must replace "YOUR_FILE"
                                        #       with a pointer to the actual file you are uploading.
                                        media_body = MediaFileUpload(path1)
                                        )
    response = requested.execute()
    print(response)
    return response

                                