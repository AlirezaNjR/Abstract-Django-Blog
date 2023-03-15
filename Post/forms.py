from django import forms
from martor.fields import MartorFormField
from .models import AudioPostModel, VideoPostModel, PhotoPostModel, TextPostModel, CategoryModel


class AudioPostForm(forms.ModelForm):
    class Meta:
        model = AudioPostModel
        exclude = ('author',)
        widget = {
            'category': forms.CheckboxSelectMultiple()
        }


class VideoPostForm(forms.ModelForm):
    class Meta:
        model = VideoPostModel
        exclude = ('author',)
        widget = {
            'category': forms.CheckboxSelectMultiple()
        }


class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPostModel
        exclude = ('author',)
        widget = {
            'category': forms.CheckboxSelectMultiple()
        }


class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPostModel
        exclude = ('author',)

#! ----------------- Edit Post Forms ---------------------
class EditAudioPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = MartorFormField()
    audio = forms.FileField(required=False)
    cover = forms.ImageField(required=False)
    slug = forms.SlugField(required=True)
    tags = forms.CharField()
    category = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class EditVideoPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = MartorFormField()
    video = forms.FileField(required=False)
    cover = forms.ImageField(required=False)
    slug = forms.SlugField(required=True)
    tags = forms.CharField()
    category = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class EditPhotoPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = MartorFormField()
    image = forms.FileField(required=False)
    slug = forms.SlugField(required=True)
    tags = forms.CharField()
    category = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
    )

class EditTextPostForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea,required=True)