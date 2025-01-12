from django.contrib import admin
from .models import GeneralStatistics

# Регистрируем модель в админке
@admin.register(GeneralStatistics)
class GeneralStatisticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)
