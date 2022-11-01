from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Index')

def base(request):
    return render(request, 'base.html')

def about(request):
    return HttpResponse('About')
