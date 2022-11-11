from email.policy import default
from enum import auto
from django.db import models
from datetime import date, datetime

class Event(models.Model):
    title=models.CharField(max_length=150)
    duration=models.DurationField()
    block=models.BooleanField(default=False)
    day=models.CharField(max_length=150)
    def __str__(self):
        #it will return the titlepython
        return self.title



