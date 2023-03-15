from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(VideoPostCommentModel)
admin.site.register(PhotoPostCommentModel)
admin.site.register(AudioPostCommentModel)

# admin.site.register(VideoPostReplyCommentModel)
# admin.site.register(PhotoPostReplyCommentModel)
# admin.site.register(AudioPostReplyCommentModel)