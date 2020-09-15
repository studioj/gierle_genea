from django.db import models
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(default=datetime(1, 1, 1, 0, 0))
