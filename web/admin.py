from django.contrib import admin

from web.models import ExtractedNews


@admin.register(ExtractedNews)
class ExtractedNewsAdmin(admin.ModelAdmin):
    list_display = (
        "news_id",
        "url",
        "title",
        "created_date",
        "text",
    )
