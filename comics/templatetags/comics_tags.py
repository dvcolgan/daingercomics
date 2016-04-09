from django.template import Library
from PIL import Image
import math
import os
from markdown import markdown as parse_markdown


register = Library()


def scale(max_x, pair):
    x, y = pair
    new_y = (float(max_x) / x) * y
    return (int(math.ceil(float(max_x))), int(math.ceil(float(new_y))))


@register.filter
def markdown(text):
    return parse_markdown(text)


@register.filter
def thumbnail(file, size='200w'):
    # defining the size
    if (size.lower().endswith('h')):
        mode = 'h'
        size = size[:-1]
        max_size = int(size.strip())
    elif (size.lower().endswith('w')):
        mode = 'w'
        size = size[:-1]
        max_size = int(size.strip())
    elif (size.lower().endswith('s')):
        mode = 's'
        size = size[:-1]
        max_size = int(size.strip())
    else:
        mode = 'both'
        
    # defining the filename and the miniature filename
    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename)>os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    # if the image wasn't already resized, resize it
    if True or not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image_x, image_y = image.size  

        if mode == 'w':
            image_x, image_y = scale(max_size, (image_x, image_y))
        elif mode == 'h':
            image_y, image_x = scale(max_size, (image_y, image_x))
        elif mode == 's':
            if image_x < image_y:
                image_x, image_y = scale(size, (image_x, image_y))
            else:
                image_y, image_x = scale(size, (image_y, image_x))
        elif mode == 'both':
            image_x, image_y = [int(x) for x in size.split('x')]
        else:
            raise Exception("Thumbnail size must be in ##w, ##h, or ##x## format.")
            
        image.thumbnail([image_x, image_y], Image.ANTIALIAS)
        if mode == 's':
            x, y = [max(0, (image_x - max_size) / 2), max(0, (image_y - max_size) / 2)]
            image = image.crop((x, y, x + max_size, y + max_size))

        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url
