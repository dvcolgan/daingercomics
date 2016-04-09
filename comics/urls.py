from django.conf.urls import url
from comics import views

urlpatterns = [
    url(r'^$', views.comic),
    url(r'^(?P<comic_id>\d+)/$', views.comic),
    url(r'^s/(?P<page_slug>[\w\d]+)/$', views.static),
]
