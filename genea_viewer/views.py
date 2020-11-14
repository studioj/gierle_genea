from datetime import datetime

from django.shortcuts import render

from genea_viewer.models import Person, BirthEvent


def index(request):
    return render(request, "home.html")


def add_person(request):
    birth_date = BirthEvent.objects.create(date=datetime.strptime(request.POST["person_birth_date"], "%Y-%m-%dT%H:%M:%S"))

    person_ = Person.objects.create(name=request.POST["person_name"], first_name=request.POST["person_first_name"], birth_event=birth_date)
    all_persons = Person.objects.all()
    return render(
        request, "home.html", {"added_person_name": person_.name, "added_person_first_name": person_.first_name, "all_persons": all_persons}
    )
