from django.urls import path
from joemascot.views import Home_View, Service_View, Contact_View, About_View


urlpatterns = [
    path('', Home_View.as_view(), name='home'),
    path('services', Service_View.as_view(), name='service'),
    path('contact', Contact_View.as_view(), name='contact'),
    path('about', About_View.as_view(), name='about'),
]
