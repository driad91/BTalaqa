from django.urls import path,re_path
from MCQAssignmentsApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    re_path(r'^login/$',
            auth_views.LoginView.as_view(template_name= 'login.html'),
            name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),


    re_path('^$', views.home
            , name='home'),
    re_path('^home/$', views.home
            , name='home'),
    re_path('^test/$', views.create_test, name='create_test'),
    re_path('questions_answers/$', views.create_questions_answers
            , name='create_question_answers')

]

