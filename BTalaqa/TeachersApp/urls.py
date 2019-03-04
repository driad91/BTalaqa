from django.urls import path,re_path
from TeachersApp import views
app_name ='TeachersApp'
urlpatterns = [



    re_path('^$', views.home
            , name='home'),
    re_path('^test/', views.create_test, name='create_test'),
    re_path('^questions_answers/(?P<pk>\d+)/$', views.create_questions_answers
            , name='create_question_answers')

]

