from django.conf.urls import patterns, url

from teams_fbv_user import views

urlpatterns = patterns('',
  url(r'^$', views.team_list, name='team_list'),
  url(r'^new$', views.team_create, name='team_new'),
  url(r'^edit/(?P<pk>\d+)$', views.team_update, name='team_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.team_delete, name='team_delete'),
)