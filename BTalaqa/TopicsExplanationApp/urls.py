from django.urls import re_path
from TopicsExplanationApp import views

app_name ='TopicsExplanationApp'

urlpatterns = [
    re_path('^active-passive/', views.render_active_passive, name='render_active_passive')
]