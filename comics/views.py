from comics.models import *
from django.shortcuts import get_object_or_404, render

def comic(request, comic_id=None):

    # Get ordered list of comics, and pull out the newest & oldest ones,
    # as well as the requested one (if a request was made)
    comics_ordered = Comic.objects.order_by('-id')
    comic_newest = comics_ordered[0]
    comic_oldest = comics_ordered.reverse()[0]
    if comic_id:
        comic = get_object_or_404(Comic, id=comic_id)
    else:
        comic = comic_newest

    # Get the ids of the next and previous comics, for the buttons
    if comic.id < comic_newest.id:
        comic_id_next = comic.id + 1
    else:
        comic_id_next = 1

    if comic.id > 1:
        comic_id_prev = comic.id - 1
    else:
        comic_id_prev = comic_newest.id

    return render(request, 'comic.html', locals())

def static(request, page_slug):
    page = get_object_or_404(StaticPage, slug=page_slug)
    return render(request, 'static.html', locals())

def privacy(request):
    return render(request, 'privacy.html', locals())
