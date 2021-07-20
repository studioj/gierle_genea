from django.db import models
import datetime
from pytz import timezone


class LifeEvent(models.Model):
    pass


class BirthEvent(LifeEvent):
    date = models.DateTimeField(null=True)


class Person(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    birth_event = models.ForeignKey(BirthEvent, models.DO_NOTHING, default=1)
    death_event = models.ForeignKey(DeathEvent, models.DO_NOTHING, blank=True, null=True)
