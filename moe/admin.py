from django.contrib import admin
from . import models


@admin.register(models.Kiroku)
class KirokuAdmin(admin.ModelAdmin):
    list_display = ("dt", "moe_cnt", "moyori_cnt",)
    list_filter = ("dt",)
    search_fields = ("dt", "moe_cnt", "moyori_cnt",)


@admin.register(models.Mokuhyo)
class MokuhyoAdmin(admin.ModelAdmin):
    list_display = ("last_moe", "last_moyori",)
    # list_filter = ("dt",)
    search_fields = ("last_moe", "last_moyori",)
