from django.http import HttpResponse
from django.shortcuts import render
import datetime

def time(request):
    time = datetime.datetime.now()
    return HttpResponse("time")

def goodbye(request):
    return HttpResponse("goodbye")
