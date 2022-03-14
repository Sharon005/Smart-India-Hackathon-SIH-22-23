from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'Web_APP'

urlpatterns = [
    path('', views.home, name="home"),
    path('crops', views.crops, name="crops"),
    path('meetings', views.meetings, name="meetings"),
    path('meeting_d', views.meeting_d, name="meeting_d"),
    
]
