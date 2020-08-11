from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the genea_gierle index.")


def add_person(request):
    return HttpResponse("Hello, add your person here")
