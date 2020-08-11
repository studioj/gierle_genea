from django.http import HttpResponse
from django.shortcuts import render

from genea_viewer.models import Person


def index(request):
    return render(request, 'home.html')


def add_person(request):
    person_ = Person.objects.create(name=request.POST['person_name'])
    all_persons = Person.objects.all()
    return render(request, 'home.html', {"added_person": person_.name, "all_persons": all_persons})
