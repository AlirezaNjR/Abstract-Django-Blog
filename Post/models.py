from django.db import models
from django.urls import reverse
from martor.models import MartorField
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from os import path as os_path, remove as os_remove 
# ! -------------------------------------------------
#! The address of the file storage location
_Videos_Path = lambda instance, filename: f'Videos/{instance.author.username}/{filename}'
_Photos_Path = lambda instance, filename: f'Images/{instance.author.username}/{filename}'
_Audios_Path = lambda instance, filename: f'Audios/{instance.author.username}/{filename}'

# ! The address of the cover storage location
_Videos_Cover_Path = lambda instance , filename : \
    f'Videos/{instance.author.username}/Covers/{filename}'
_Audios_Cover_Path = lambda instance , filename : \
    f'Audios/{instance.author.username}/Covers/{filename}'
    
#! ---------------------------- Models ---------------------------------

class CategoryModel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class VideoPostModel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = MartorField(null=False, blank=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='VideosAuthor'
    )
    video = models.FileField(
        upload_to=_Videos_Path, blank=False, null=False)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)
    category = models.ManyToManyField(
        CategoryModel, related_name='VideoCategory')
    cover = models.ImageField(
        upload_to=_Videos_Cover_Path, blank=True, null=True)
    slug = models.SlugField(
        max_length=26,
        unique=True,
        null=False,
        blank=False
    )
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("Post:Video_Detail", kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Video Post'
        verbose_name_plural = 'Video Posts'

    def __str__(self):
        return str(self.title) + " " + str(self.author)

    def _delete_file_(self, video=False, cover=False):
        if video:
            if os_path.isfile(self.video.path):
                os_remove(self.video.path)
        if cover:
            try:
                os_path.isfile(self.cover.path)
                os_remove(self.cover.path)
            except:
                print(f'From Video Post : There is a problem deleting the cover file')


class PhotoPostModel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = MartorField(null=False, blank=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='PhotosAuthor'
    )
    image = models.ImageField(
        upload_to=_Photos_Path, blank=False, null=False)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)
    category = models.ManyToManyField(
        CategoryModel, related_name='PhotoCategory')
    slug = models.SlugField(
        max_length=26,
        unique=True,
        null=False,
        blank=False
    )
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("Post:Photo_Detail", kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Photo Post'
        verbose_name_plural = 'Photo Posts'

    def __str__(self):
        return str(self.title) + " " + str(self.author)

    def _delete_file_(self):
        if os_path.isfile(self.image.path):
            os_remove(self.image.path)


class AudioPostModel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = MartorField(null=False, blank=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='AudiosAuthor'
    )
    audio = models.FileField(
        upload_to=_Audios_Path, blank=False, null=False)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)
    category = models.ManyToManyField(
        CategoryModel, related_name='AudioCategory')
    cover = models.ImageField(
        upload_to=_Audios_Cover_Path, blank=True, null=True)
    slug = models.SlugField(
        max_length=26,
        unique=True,
        null=False,
        blank=False
    )
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("Post:Audio_Detail", kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Audio Post'
        verbose_name_plural = 'Audio Posts'

    def __str__(self):
        return str(self.title) + " " + str(self.author)

    def _delete_file_(self, audio=False, cover=False):
        if audio:
            if os_path.isfile(self.audio.path):
                os_remove(self.audio.path)
        if cover:
            try:
                os_path.isfile(self.cover.path)
                os_remove(self.cover.path)
            except:
                print(f'From Audio Post : There is a problem deleting the cover file')


class TextPostModel(models.Model):
    body = models.TextField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='TextAuthor'
    )
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Text Post'
        verbose_name_plural = 'Text Posts'

    def __str__(self):
        return str(self.body) + " " + str(self.author)
