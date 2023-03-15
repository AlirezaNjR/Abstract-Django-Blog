from django.db import models
from django.contrib import admin
from martor.admin import AdminMartorWidget
from .models import VideoPostModel, PhotoPostModel, AudioPostModel, TextPostModel, CategoryModel
# Register your models here.


class VideoPostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }
admin.site.register(VideoPostModel, VideoPostModelAdmin)

class AudioPostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }
admin.site.register(AudioPostModel, AudioPostModelAdmin)

class PhotoPostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }
admin.site.register(PhotoPostModel, PhotoPostModelAdmin)

class TextPostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }
admin.site.register(TextPostModel, TextPostModelAdmin)

admin.site.register(CategoryModel)
