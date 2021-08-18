from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def listviewdisplaydata(request):
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__sector_name__contains="Automotive") \
    .filter(rating_debt__debt_org__org_name__contains="Range Rover" ) \
    .filter(rating_debt__debt_name__contains="debt_name_2")
    return render(request, "Index.html", {'Ratings': results})

def orgdashboard(request):
    results = Sector.objects.all();
    return render(request, "orgdashboard.html", {'Sectors': results})

def sectororogs(request, sector_id):
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__id=sector_id )
    return render(request, "Index.html", {'Ratings': results})

def sectororogdebts(request, sector_id, org_name):
    print(org_name)
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__id=sector_id ) \
    .filter( rating_debt__debt_org__org_name__contains=org_name )
    return render(request, "Index.html", {'Ratings': results})