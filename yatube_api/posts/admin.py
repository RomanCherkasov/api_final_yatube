from django.contrib import admin

from .models import Follow


# Register your models here.


class Follows(admin.ModelAdmin):
    list_display = ('pk', 'following', 'user')


admin.site.register(Follow, Follows)
