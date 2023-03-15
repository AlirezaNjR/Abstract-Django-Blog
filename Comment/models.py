from django.db import models
from django.contrib.auth import get_user_model
from Post.models import AudioPostModel, VideoPostModel, PhotoPostModel

# Create your models here.
class AudioPostCommentModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    website = models.URLField(max_length=300, null=True, blank=True)
    message = models.TextField(max_length=700, null=False, blank=False)
    post = models.ForeignKey(AudioPostModel, on_delete=models.CASCADE,related_name='Comments', null=False, blank=False)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True,blank=True)   
    class Meta:
        ordering = ['-datetime',]
        verbose_name = 'Comment On Audio Post'
        verbose_name_plural = 'Comments On Audio Posts' 

    def __str__(self) -> str:
        return f'{self.name} On {self.post}'


class VideoPostCommentModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    website = models.URLField(max_length=300, null=True, blank=True)
    message = models.TextField(max_length=700, null=False, blank=False)
    post = models.ForeignKey(VideoPostModel, on_delete=models.CASCADE,related_name='Comments', null=False, blank=False)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        ordering = ['-datetime',]
        verbose_name = 'Comment On Video Post'
        verbose_name_plural = 'Comments On Video Posts' 

    def __str__(self) -> str:
        return f'{self.name} On {self.post}'


class PhotoPostCommentModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    website = models.URLField(max_length=300, null=True, blank=True)
    message = models.TextField(max_length=700, null=False, blank=False)
    post = models.ForeignKey(PhotoPostModel, on_delete=models.CASCADE,related_name='Comments', null=False, blank=False)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)
    user = models.ForeignKey(get_user_model(),related_name='UserCommenter',on_delete=models.SET_NULL,null=True,blank=True)
  
    class Meta:
        ordering = ['-datetime',]
        verbose_name = 'Comment On Photo Post'
        verbose_name_plural = 'Comments On Photo Posts' 

    def __str__(self) -> str:
        return f'{self.name} On {self.post}'

