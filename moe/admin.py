from django.contrib import admin
from . import models


@admin.register(models.Kiroku)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("dt", "moe_cnt", "moyori_cnt",)
    list_filter = ("dt",)
    search_fields = ("dt", "moe_cnt", "moyori_cnt",)
