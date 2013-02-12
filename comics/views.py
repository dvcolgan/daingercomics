from django.template import Context, loader
from comics.models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from markdown import markdown
import random
import math
from settings import PAGE_MAX_WIDTH, PAGE_MAX_HEIGHT, PAGE_BACKGROUND_THUMB_SIZE

def comic(request, comic_id=None):

    # Get ordered list of comics, and pull out the newest & oldest ones,
    # as well as the requested one (if a request was made)
    comics_ordered = Comic.objects.order_by('-id')
    comic_newest = comics_ordered[0]
    comic_oldest = comics_ordered.reverse()[0]
    if comic_id: comic = get_object_or_404(Comic, id=comic_id)
    else:        comic = comic_newest

    # Get the ids of the next and previous comics, for the buttons
    if comic.id < comic_newest.id: comic_id_next = comic.id + 1
    else:                          comic_id_next = 1

    if comic.id > 1: comic_id_prev = comic.id - 1
    else:            comic_id_prev = comic_newest.id

    # Generate lists of the background images
    background_image_rows = generate_background_image_lists(comics_ordered)

    # Render to the template
    return render(request, 'comic.html', locals())

def static(request, page_slug):

    # Get the static-page object
    page = get_object_or_404(StaticPage, slug=page_slug)

    # Generate lists of the background images
    background_image_rows = generate_background_image_lists(Comic.objects.order_by('-id'))

    # Render to the template
    return render(request, 'static.html', locals())

def privacy(request):
    background_image_rows = generate_background_image_lists(Comic.objects.all())
    return render(request, 'privacy.html', locals())

# Helpers

def generate_background_image_lists(comics):
    
    # Make a list of images that can be used in the background & shuffle it
    background_images = []
    #for c in comics: background_images.append(c.image)
    for c in BackgroundImage.objects.all(): background_images.append(c.image)
    random.shuffle(background_images)

    # Make a list of rows of images with which to fill the background
    n_rows = int(math.ceil(PAGE_MAX_HEIGHT / PAGE_BACKGROUND_THUMB_SIZE))
    n_cols = int(math.ceil(PAGE_MAX_WIDTH / PAGE_BACKGROUND_THUMB_SIZE))
    background_image_rows = []
    i_img = 0
    for i_row in range(n_rows):
        background_image_rows.append([])
        for i_col in range(n_cols):
            background_image_rows[i_row].append(background_images[i_img])
            i_img += 1
            if i_img >= len(background_images):
                random.shuffle(background_images)
                i_img = 0

    return background_image_rows
