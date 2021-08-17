from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Listviewdisplaydata(request):
    results = Ratings.objects.all()
    return render(request, "Index.html", {'Ratings': results})