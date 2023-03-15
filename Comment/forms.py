from django import forms

class AnonymousCommentForm(forms.Form):
    name = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=255, required=True)
    website = forms.URLField(max_length=300,required=False)
    message = forms.CharField(widget=forms.Textarea,max_length=700,required=True)

class UserCommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea,max_length=700,required=True)
    