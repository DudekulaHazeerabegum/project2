from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project2(request):
    return HttpResponse('<marquee><h1> MY FIRST PROJECT APPLICATION IS SUCCESSFULL</h1></marquee>')

