from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World!")


def newproduct(request):
    return HttpResponse("New Product")
