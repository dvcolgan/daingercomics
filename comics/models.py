from django.db import models


class Comic(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/')
    image_title = models.CharField(max_length=511, blank=True)
    image_alt = models.CharField(max_length=511, blank=True)
    post = models.TextField(blank=True)
    date = models.DateField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % self.id


class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='img/')

    def __unicode__(self):
        return self.image.path


class StaticPage(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
        return self.title
