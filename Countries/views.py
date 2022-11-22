from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .parser import parser


def index(request: HttpRequest) -> HttpResponse:
    template = 'index.html'
    context = {}
    return render(request, template, context)


def countries(request: HttpRequest) -> HttpResponse:
    template = 'countries.html'
    context = {"countries":parser.get_countries()}
    return render(request, template, context)


def country(request: HttpRequest) -> HttpResponse:
    country_id = request.GET.get('name', 0)

    if not country_id:
        return HttpResponse("Page not found")
    
    template = 'country.html'
    context = {
            'country': country_id,
            'langs': parser.get_langs(country_id),
        }
    
    return render(request, template, context)
