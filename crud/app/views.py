from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def khan(request):
    return HttpResponse("<h2>My name is khan</h2>")


def index(request):
    return render(request, "app/index.html")
