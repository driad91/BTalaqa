from django.urls import path,re_path
from MCQAssignmentsApp import views
app_name ='MCQAssignmentsApp'
urlpatterns = [
    re_path('^test/', views.create_test, name='create_test'),
    re_path('^questions_answers/(?P<pk>\d+)/$', views.create_questions_answers
            , name='create_question_answers'),
    re_path('^students_assignments/', views.students_assignments
            , name='students_assignments')

]

