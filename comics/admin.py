from comics.models import *
from django.contrib import admin

admin.site.register(Comic)
admin.site.register(BackgroundImage)

class StaticPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(StaticPage, StaticPageAdmin)
