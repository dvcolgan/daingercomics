from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from comics.feeds import *
from comics import urls as comics_urls
from settings import MEDIA_ROOT

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': '/static/'}),
    url(r'^rss/$', ComicsFeed()),
    url(r'', include(comics_urls)),
    url(r'^admin/', admin.site.urls),
]
