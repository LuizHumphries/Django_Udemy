from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request) -> HttpResponse:
    return render(request, "recipes/home.html")


def sobre(request) -> HttpResponse:
    return HttpResponse("SOBRE")


def contato(request) -> HttpResponse:
    return HttpResponse("CONTATO")
