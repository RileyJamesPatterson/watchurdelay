from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Flight
from django.core import serializers
from django.http import JsonResponse

def index(request):
    return render(request,'home.html',{})

def pivot_data(request):
    'a method to serve pivot table data'
    dataset = Flight.objects.filter(OriginCityName="Atlanta, GA") #HARDCODED FILTER FOR NOW TO REDUCE DATA SIZE
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)