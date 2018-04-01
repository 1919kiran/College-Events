from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.test, name='test'),
    #path('', views.signup, name='test'),
]
