from django.urls import path
from .views import subscription_view , contact_us_view , about_page_view 

app_name = 'Main'

urlpatterns = [
    path('Subscribe/',subscription_view,name='Subscription'), # type: ignore
    path('Contact/',contact_us_view,name='Contact'),
    path('About/', about_page_view, name='About'),
    
]
 