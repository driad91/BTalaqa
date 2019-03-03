from django.urls import path,re_path
from StudentsApp import views

from django.contrib.auth import views as auth_views
app_name = 'StudentsApp'
urlpatterns = [
re_path('^$', views.home, name='home'),
re_path('^home/$', views.home, name='home')
]