from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Flight,Airport
from django.core import serializers
from django.http import JsonResponse

def index(request):
    airports=serializers.serialize('json',Airport.objects.all())
    context={
        "airports":airports
    }
    return render(request,'index.html',context)

def pivot_data(request): #currently unused - pivot table index changed
    'a method to serve pivot table data'
    dataset = Flight.objects.filter(OriginCityName="Atlanta, GA") #HARDCODED FILTER FOR NOW TO REDUCE DATA SIZE
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)