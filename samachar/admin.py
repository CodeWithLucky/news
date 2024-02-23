from django.contrib import admin
from . models import NewsModel

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'description', 'date'
    ]

admin.site.register(NewsModel, NewsAdmin)