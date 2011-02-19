from django.conf.urls.defaults import *


urlpatterns = patterns('apps.core.views',
    url('^$', 'test', name='test')
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
)

  