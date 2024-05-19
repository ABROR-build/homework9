from django.contrib import admin
from . import models


class BlogConfig(admin.ModelAdmin):
    list_display = ['author', 'title', 'summary']


admin.site.register(models.Blogs, BlogConfig)
