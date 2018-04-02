from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('', views.test, name='test'),
]
