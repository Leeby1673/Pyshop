from django.http import HttpResponse
from django.shortcuts import render
from .models import Person


def index(request):
    persons = Person.objects.all()
    return render(
        request,
        "index.html",
        {"persons": persons},
    )


def newproduct(request):
    return HttpResponse("New Product")
