from django.contrib.syndication.views import Feed
from comics.models import *
from markdown import markdown

class ComicsFeed(Feed):
    title = "Dainger Comics Update Feed"
    link = "/"
    description = "New Dainger Comics delivered to your feed reader!"

    def items(self):
        return Comic.objects.order_by('-id')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.post)
