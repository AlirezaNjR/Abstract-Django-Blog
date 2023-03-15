from django.urls import path
from .views import home_page_view, audio_post_detail_view, \
    video_post_detail_view, photo_post_detail_view, category_view, search_view,\
    new_audio_post_view, new_video_post_view, new_photo_post_view, new_text_post_view, select_view, \
    edit_audio_post_view, edit_video_post_view, edit_photo_post_view, edit_text_post_view,\
    delete_audio_post_view, delete_photo_post_view, delete_text_post_view, delete_video_post_view

app_name = 'Post'

urlpatterns = [
    path('', home_page_view, name='Home'),
    path('Search/', search_view, name='Search'),
    path('Category/<str:category>/', category_view, name="Category_Filter"),

    # ! New Post Urls
    path('Select/', select_view, name='Select'),
    path('Audio/Create/', new_audio_post_view, name='Create_AudioPost'),
    path('Video/Create/', new_video_post_view, name='Create_VideoPost'),
    path('Photo/Create/', new_photo_post_view, name='Create_PhotoPost'),
    path('Text/Create/', new_text_post_view, name='Create_TextPost'),

    # ! Detail Post Urls
    path('Audio/Detail/<slug:slug>/', audio_post_detail_view, name='Audio_Detail'),
    path('Video/Detail/<slug:slug>/', video_post_detail_view, name='Video_Detail'),
    path('Photo/Detail/<slug:slug>/', photo_post_detail_view, name='Photo_Detail'),

    # ! Edit Post Urls
    path('Audio/Edit/<int:post_id>/', edit_audio_post_view, name='Edit_AudioPost'),
    path('Video/Edit/<int:post_id>/', edit_video_post_view, name='Edit_VideoPost'),
    path('Photo/Edit/<int:post_id>/', edit_photo_post_view, name='Edit_PhotoPost'),
    path('Text/Edit/<int:post_id>/', edit_text_post_view, name='Edit_TextPost'),

    # ! Delete Post Urls
    path('Audio/Delete/<int:pk>', delete_audio_post_view, name='Delete_AudioPost'),
    path('Video/Delete/<int:pk>', delete_video_post_view, name='Delete_VideoPost'),
    path('Photo/Delete/<int:pk>', delete_photo_post_view, name='Delete_PhotoPost'),
    path('Text/Delete/<int:pk>', delete_text_post_view, name='Delete_TextPost'),
]
