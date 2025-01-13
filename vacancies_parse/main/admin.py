from django.contrib import admin
from .models import GeneralStatistics, DemandStatistics, Geography


# Регистрируем модель в админке
@admin.register(GeneralStatistics)
class GeneralStatisticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)


@admin.register(DemandStatistics)
class DemandStatisticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)

@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)