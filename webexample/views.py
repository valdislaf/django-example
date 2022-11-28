from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

def index(request):
     return HttpResponse("<h1>This is a H1 heading!</h1><h2>This is a H2 heading!</h2><h3>This is a H3 heading!</h3>")


# from django.shortcuts import render

# def index (request):
#     return render(request, 'C:/Users/aldes/Desktop/django-examples/mysite/webexample/zTopModel/index.html')

# Create your views here.
