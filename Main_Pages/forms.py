from django import forms

class EmailSubscriptionsForm(forms.Form):
    email = forms.EmailField(max_length=256,required=True)
    
class ContactForm(forms.Form):
    name = forms.CharField(required=True,max_length=255)
    email = forms.EmailField(required=True)
    website = forms.CharField(max_length=255,required=False)
    message = forms.CharField(widget=forms.Textarea,max_length=700,required=True)