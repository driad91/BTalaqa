from django.urls import path,re_path
from MCQAssignmentsApp import views

urlpatterns = [
    re_path('test/$', views.create_test, name='create_test'),
    re_path('questions_answers/$', views.create_questions_answers
            , name='create_question_answers')

]

