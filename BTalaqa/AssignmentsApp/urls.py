from django.urls import path,re_path
from AssignmentsApp import views
app_name ='AssignmentsApp'
urlpatterns = [

    re_path('^assign_users/', views.assign_users, name='assign_users_tests'),


]

