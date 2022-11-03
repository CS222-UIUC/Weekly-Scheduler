from email.policy import default
from enum import auto
from django.db import models
from datetime import date, datetime

class Day(models.Model):
    day=models.CharField(max_length=10)
    start=models.TimeField(default='8:00:00')

class Event(models.Model):
    title=models.CharField(max_length=150)
    duration=models.DurationField()
    block=models.BooleanField(default=False)
    day=models.ForeignKey(Day, to_field='day', on_delete=models.SET_DEFAULT)
    def __str__(self):
        #it will return the titlepython
        return self.title



