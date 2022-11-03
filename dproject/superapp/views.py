from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms import UserForm
from .models import Person


# Create your views here.


def index(request):
    # if request.method == "POST":
        # name = request.POST.get("name") # получить значение поля Имя
        # age = request.POST.get("age")  # получить значение поля Возраст
        # town = request.POST.get("town")
        # output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}, Город - {2}  </hЗ>".format(name, age, town)
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
        # return HttpResponse(output)
    # else:
    #     userform = UserForm()
    #     return render(request, "index.html", {"form": userform})


def create(request):
    if request.method == 'POST':
        klient = Person()
        klient.name = request.POST.get('name')
        klient.age = request.POST.get('age')
        klient.save()
    return HttpResponseRedirect('/')
def base(request):
    some_list = [2 ** x for x in range(50)]
    some_string = ' '.join(map(str, some_list))
    return render(request, 'base.html', {'name': some_string})


def about():
    return HttpResponse('About')
