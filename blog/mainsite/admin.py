from django.contrib import admin

# Register your models here.

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date','like_count')

class VideoAdmin(admin.ModelAdmin):
    list_display=('title','slug','src','pub_date')

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Video,VideoAdmin)