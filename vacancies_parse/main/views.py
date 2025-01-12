from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneralStatistics

def index(request):
    return render(request, 'main/index.html')

def general_statistics(request):
    # Получаем все данные из модели GeneralStatistics
    statistics_sections = GeneralStatistics.objects.all
    context = {
        'sections': statistics_sections
    }
    return render(request, 'main/general_statistics.html', context)


