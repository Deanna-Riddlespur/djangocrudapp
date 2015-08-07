from django.conf.urls import patterns, url

from teams_cbv import views

urlpatterns = patterns('',
  url(r'^$', views.TeamList.as_view(), name='team_list'),
  url(r'^new$', views.TeamCreate.as_view(), name='team_new'),
  url(r'^edit/(?P<pk>\d+)$', views.TeamUpdate.as_view(), name='team_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.TeamDelete.as_view(), name='team_delete'),
)