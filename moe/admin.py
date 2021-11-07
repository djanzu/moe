from django.contrib import admin
from . import models


@admin.register(models.Sengakuji)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("dt", "cnt",)
    list_filter = ("dt", "cnt",)
    search_fields = ("dt", "cnt",)


@admin.register(models.Moework)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("dt", "cnt",)
    list_filter = ("dt", "cnt",)
    search_fields = ("dt", "cnt",)

