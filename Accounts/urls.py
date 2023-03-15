from .views import sign_up, profile
from django.urls import path, include

app_name = 'Accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('SignUp/', sign_up, name='SignUp'),
    path('Profile/<int:id>', profile, name='Profile')
]
