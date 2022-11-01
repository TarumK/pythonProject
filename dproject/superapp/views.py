from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import UserForm

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get("name") # получить значение поля Имя
        age = request.POST.get("age")  # получить значение поля Возраст
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1} </hЗ>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


def base(request):
    some_list = [2 ** x for x in range(50)]
    some_string = ' '.join(map(str, some_list))
    return render(request, 'base.html', {'name': some_string})


def about():
    return HttpResponse('About')
