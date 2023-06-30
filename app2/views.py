from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def project1(request):
    return HttpResponse('<marquee><h1>THIS IS MY FIRST PROJECT APPLICATION</marquee></h1>')


def project(request):
    return render(request,'project.html')