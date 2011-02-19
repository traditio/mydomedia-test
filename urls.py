from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^', include('apps.core.urls')),
    (r'^admin/', include(admin.site.urls)),
)
