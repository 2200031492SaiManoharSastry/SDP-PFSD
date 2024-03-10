
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests


def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def contactfunction(request):
    return render(request,"contact.html")

def loginfunction(request):
    return render(request,"login.html")

def servicesfunction(request):
    return render(request,"services.html")

def registrationfunction(request):
    return render(request,"register.html")

def register(request):
    forms= register()

def dailyhoroscope(request):
    return render(request,"dailyhoroscope.html")

def horoscope(request):
    return render(request,"horoscope.html")

def forget(request):
    return render(request,"forget.html")
def nakshatra(request):
    return render(request,"nakshatra.html")

def input1(request):
    return render(request, "nakshatra.html")
