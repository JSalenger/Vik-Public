#-*- coding: utf-8 -*-
#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = "polls"
urlpatterns = [
    url(r'^$', views.QuestionListView, name='home'),
    url(r'^(?P<poll_id>\d+)/$', views.DetailView, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^create/$', views.PollCreateView.as_view(), name='create')
]
