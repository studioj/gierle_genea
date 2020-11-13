from django.db import models
import datetime


class Person(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)


class LifeEvent(models.Model):
    pass


class BirthEvent(LifeEvent):
    date = models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0))
