from django.urls import re_path
from MCQAssignmentsApp import views

app_name ='MCQAssignmentsApp'

urlpatterns = [
    re_path('^test/', views.create_test, name='create_test'),
    re_path('^questions_answers/(?P<pk>\d+)/$', views.create_questions_answers
            , name='create_question_answers'),
    re_path('^students_assignments/', views.students_assignments
            , name='students_assignments'),
    re_path('^render_test/(?P<id>\d+)/$', views.render_test
            , name='render_test'),
    re_path('submit_test/', views.submit_test
            , name='submit_test'),
    re_path('^overview/(?P<pk>\d+)/$', views.test_overview
            , name='test_overview'),
    re_path('^delete_question/(?P<pk>\d+)/(?P<question_pk>\d+)/$', views.delete_question
            , name='delete_question'),
    re_path('^dashboard/', views.dashboard, name='dashboard')
]

