from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
    re_path(r'^home/(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
]
