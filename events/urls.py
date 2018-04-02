from django.urls import path, re_path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_index, name='index'),
    re_path(r'^(?P<slug>[\w-]+)', views.event_detail, name="detail"),
]
