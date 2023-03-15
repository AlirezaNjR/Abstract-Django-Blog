from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# ! The address of the file storage location
_Users_Image_Path = lambda instance , filename: f'Users/{instance.username}/{filename}'


class CustomUserModel(AbstractUser):
    
    bio = models.TextField(max_length=300,null=False,blank=False)
    image = models.ImageField(upload_to=_Users_Image_Path,null=True,blank=True)
    instagram = models.URLField(max_length=200,null=True,blank=True)
    telegram = models.URLField(max_length=200,null=True,blank=True)
    site = models.URLField(max_length=200,null=True,blank=True)