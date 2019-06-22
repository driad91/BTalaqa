from django.urls import re_path
from MCQAssignmentsApp import views

app_name ='MCQAssignmentsApp'

urlpatterns = [
    re_path('^test/', views.create_test, name='create_test'),
    re_path('^questions_answers/(?P<pk>\d+)/$', views.create_questions_answers
            , name='create_question_answers'),
    re_path('^students_assignments/', views.students_assignments
            , name='students_assignments'),
    re_path('^render_test/(?P<id>\d+)/(?P<student_id>\d+)/$', views.render_test
            , name='render_test'),
    re_path('submit_test/', views.submit_test
            , name='submit_test'),
    re_path('^overview/(?P<pk>\d+)/$', views.test_overview
            , name='test_overview'),
    re_path('^delete_question/(?P<pk>\d+)/(?P<question_pk>\d+)/$', views.delete_question
            , name='delete_question'),
    re_path('delete_test/(?P<pk>\d+)/$', views.delete_test
            , name='delete_test'),
    re_path('^edit_tests/', views.edit_tests, name='edit_tests'),
    re_path('^render_teacher_dashboard/', views.render_teacher_dashboard, name='render_teacher_dashboard'),

    re_path('^assign_users/', views.assign_users, name='assign_users_tests'),
    re_path('^render_student_dashboard/(?P<user_id>\d+)/$', views.render_student_dashboard, name='render_student_dashboard'),
    re_path('^render_videos/$', views.render_videos, name='render_videos'),
    re_path('like_video/$', views.like_video, name='like_video'),
    re_path('students_home/$', views.render_students_home, name='students_home'),
    re_path('teachers_home/$', views.render_teachers_home, name='teachers_home')

]

