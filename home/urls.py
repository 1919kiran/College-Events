from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.about, name='about'),
    re_path(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
]
