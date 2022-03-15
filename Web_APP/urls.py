from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'Web_APP'

urlpatterns = [
    path('', views.home, name="home"),
    path('crops', views.crops, name="crops"),
    path('disease', views.disease, name="disease"),
    path('crop_result', views.crop_result, name="crop_result"),

    url(r'^wheat_disease/$', views.WheatDView.as_view(), name='wheat'),
    url(r'^wheat_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.WheatView.as_view(), name='wheat_disease'),

    
]
