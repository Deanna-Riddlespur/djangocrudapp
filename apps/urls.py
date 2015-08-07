from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teams_cbv/', include('teams_cbv.urls', namespace='teams_cbv')),
    url(r'^teams_fbv/', include('teams_fbv.urls', namespace='teams_fbv')),
    url(r'^teams_fbv_user/', include('teams_fbv_user.urls', namespace='teams_fbv_user')),
    url(r'^$', 'apps.views.home'),
]
