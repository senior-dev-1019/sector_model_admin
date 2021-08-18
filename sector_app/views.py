from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Listviewdisplaydata(request):
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__sector_name__contains="Automotive").filter(rating_debt__debt_org__org_name__contains="Range Rover" ).filter(rating_debt__debt_name__contains="debt_name_2")
    return render(request, "Index.html", {'Ratings': results})