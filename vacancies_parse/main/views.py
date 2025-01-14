from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneralStatistics, DemandStatistics, Geography, Skills

def index(request):
    return render(request, 'main/index.html')

def general_statistics(request):
    # Получаем все данные из модели GeneralStatistics
    statistics_sections = GeneralStatistics.objects.all
    context = {
        'sections': statistics_sections
    }
    return render(request, 'main/general_statistics.html', context)


def demand_page(request):
    demand_sections = DemandStatistics.objects.all
    context = {
        'sections': demand_sections
    }
    return render(request, 'main/demand_page.html', context)

def geography_statistics(request):
    geography_sections = Geography.objects.all
    context = {
        'sections': geography_sections
    }
    return render(request, 'main/geography.html', context)

def skills_statistics(request):
    skills_sections = Skills.objects.all
    context = {
        'sections': skills_sections
    }
    return render(request, 'main/skills.html', context)