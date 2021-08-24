from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models.functions import Length
from django.utils import timezone
import csv

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def listviewdisplaydata(request):
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__sector_name__contains="Automotive") \
    .filter(rating_debt__debt_org__org_name__contains="Range Rover" ) \
    .filter(rating_debt__debt_name__contains="debt_name_2")
    return render(request, "Index.html", {'Ratings': results})

def orgdashboard(request):
    results = {}
    results["level_1"] = Sector.objects.annotate(length=Length('code')).filter(length=2)
    results["level_2"] = Sector.objects.annotate(length=Length('code')).filter(length=3)
    results["level_3"] = Sector.objects.annotate(length=Length('code')).filter(length=4)
    results["level_4"] = Sector.objects.annotate(length=Length('code')).filter(length=5)
    results["level_5"] = Sector.objects.annotate(length=Length('code')).filter(length=6)
    return render(request, "orgdashboard.html", {'Sectors': results})

def sectororogs(request, sector_id):
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__id=sector_id )
    return render(request, "Index.html", {'Ratings': results})

def sectororogdebts(request, sector_id, org_name):
    print(org_name)
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__id=sector_id ) \
    .filter( rating_debt__debt_org__org_name__contains=org_name )
    return render(request, "Index.html", {'Ratings': results})

def importsector(request):
    with open('D:/Django/import.txt', 'r') as fp:
        sectors = csv.reader(fp, delimiter='|')
        row = 0
        for sector_csv in sectors:
            if row==0:
                headers = sector_csv
                row = row + 1
            else:
                # create a dictionary of sector details
                new_sector_details = {}
                for i in range(len(headers)):
                    new_sector_details[headers[i]] = sector_csv[i]
                    
                # create an instance of sector model
                new_sector = Sector()
                new_sector.__dict__.update(new_sector_details)
                new_sector.save()
                row = row + 1
        fp.close()
    results = Ratings.objects.filter( rating_debt__debt_org__org_sector__id=sector_id )
    return render(request, "Index.html", {'Ratings': results})
