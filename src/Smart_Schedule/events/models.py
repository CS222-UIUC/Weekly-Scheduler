from email.policy import default
from enum import auto
from django.db import models
from datetime import date, datetime, timedelta

class Event(models.Model):
    title=models.CharField(max_length=150)
    duration=models.DurationField()
    block=models.BooleanField(default=False)
    day=models.CharField(max_length=150)
    def __str__(self):
        #it will return the titlepython
        return self.title

class FinalManager(models.Manager):
    def create_Finalized(self, title, duration, start, day):
        if duration > timedelta(hours=1):
            self.create(title=title,start=start, end = start + timedelta(hours=1), day=day)
            self.create(title='break',start = start + timedelta(hours=1), end = start + timedelta(hours=1, minutes=15), day=day)
            nextdur = duration - timedelta(hours=1)
            finalized = FinalManager.create_Finalized(self, title=title, duration=nextdur,start=start + timedelta(hours=1, minutes=15),day=day)
        else:
            finalized = self.create(title=title, start=start, end=start+duration, day=day)
        return finalized
class Finalized(models.Model):
    title=models.CharField(max_length=150)
    start=models.TimeField()
    end=models.TimeField()
    day=models.CharField(max_length=150)
    objects = FinalManager()
    def __str__(self):
        #it will return the titlepython
        return self.title


