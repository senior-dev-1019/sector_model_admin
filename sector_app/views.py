from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Listviewdisplaydata(request):
    results = Ratings.objects.select_related('rating_debt__debt_org').all()
    print(results[0])
    return render(request, "Index.html", {'Ratings': results})
    # ratingFiles = Ratings.objects.filter( 'rating_date').select_related('rating_debt')
    # return HttpResponse("Hello, world. You're at the polls index.")