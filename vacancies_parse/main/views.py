from django.shortcuts import render
from .models import GeneralStatistics, DemandStatistics, Geography, Skills, Vacancy
import requests
from datetime import datetime, timedelta


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


def get_vacancies():
    date_to = datetime.now()
    date_from = date_to - timedelta(days=1)

    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "qa OR test OR тест OR quality assurance",
        "date_from": date_from.strftime("%Y-%m-%dT%H:%M:%S"),
        "date_to": date_to.strftime("%Y-%m-%dT%H:%M:%S"),
        "per_page": 10,
        "page": 0,
    }

    headers = {"User-Agent": "DjangoApp/1.0"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        vacancies = response.json().get("items", [])
        detailed_vacancies = []

        for vacancy in vacancies:
            if not contains_keywords(vacancy["name"], ["qa", "test", "тест", "uality assurance"]):
                continue

            vacancy_id = vacancy["id"]
            vacancy_details = requests.get(f"{url}/{vacancy_id}", headers=headers).json()

            detailed_vacancies.append({
                "name": vacancy_details.get("name"),
                "description": vacancy_details.get("description", None),
                "skills": ", ".join(skill["name"] for skill in vacancy_details.get("key_skills", [])),
                "company": vacancy_details.get("employer", {}).get("name", None),
                "salary": format_salary(vacancy_details.get("salary")),
                "region": vacancy_details.get("area", {}).get("name", None),
                "published_at": format_date(vacancy_details.get("published_at")),
            })

        return detailed_vacancies
    else:
        return None

def contains_keywords(text, keywords):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)

def format_salary(salary):
    if not salary:
        return None
    if salary["from"] and salary["to"]:
        return f"{salary['from']} - {salary['to']} {salary['currency']}"
    elif salary["from"]:
        return f"От {salary['from']} {salary['currency']}"
    elif salary["to"]:
        return f"До {salary['to']} {salary['currency']}"
    return None

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        return date_obj.strftime("%d.%m.%Y, %H:%M")
    except ValueError:
        return None

def latest_vacancies(request):
    vacancies = get_vacancies()
    return render(request, "main/latest_vacancies.html", {"vacancies": vacancies})