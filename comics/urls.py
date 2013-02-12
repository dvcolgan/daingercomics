from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('comics.views',
    url(r'^$', 'comic'),
    url(r'^(?P<comic_id>\d+)/$', 'comic'),
    url(r'^s/(?P<page_slug>[\w\d]+)/$', 'static'),
)
