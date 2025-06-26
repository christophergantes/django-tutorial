from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  # return HttpResponse("Hello World!");

  return render(request, 'home.html')

def about(request):
  # return HttpResponse("Sup! Here's some information about me")

  return render(request, 'about.html')
