from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from helpers.views import static_view

urlpatterns = patterns('',
    url(r'^$', static_view, name="home"),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    # Show the template views
    (r"^().*)$", static_view)
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name="media"),
    )
