from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Index')


def base(request):
    some_list = [2 ** x for x in range(50)]
    some_string = ' '.join(map(str, some_list))
    return render(request, 'base.html', {'name': some_string})


def about():
    return HttpResponse('About')
