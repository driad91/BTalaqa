from django.urls import re_path
from MCQAssignmentsApp import views

app_name ='MCQAssignmentsApp'

urlpatterns = [
    re_path('^test/', views.create_test, name='create_test'),
    re_path('^questions_answers/(?P<pk>\d+)/$', views.create_questions_answers
            , name='create_question_answers'),
    re_path('^overview/(?P<pk>\d+)/$', views.test_overview
            , name='test_overview'),
    re_path('^delete_question/(?P<pk>\d+)/(?P<question_pk>\d+)/$', views.delete_question
            , name='delete_question'),
    re_path('^dashboard/', views.dashboard, name='dashboard')
]

