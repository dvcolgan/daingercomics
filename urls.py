from django.conf.urls import patterns, include, url
from django.contrib import admin
from settings import MEDIA_ROOT
from comics.feeds import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^rss/$', ComicsFeed()),
    url(r'', include('comics.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
