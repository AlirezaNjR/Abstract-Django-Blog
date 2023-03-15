from django.urls import path
from .views import add_audio_post_comment , add_photo_post_comment , add_video_post_comment

app_name = 'Comment'

urlpatterns = [
    path('Comment/Add/AudioPost/<slug:slug>',add_audio_post_comment,name='Add_AudioPost_Comment'),
    path('Comment/Add/VideoPost/<slug:slug>',add_video_post_comment,name='Add_VideoPost_Comment'),
    path('Comment/Add/PhotoPost/<slug:slug>',add_photo_post_comment,name='Add_PhotoPost_Comment'),
]
