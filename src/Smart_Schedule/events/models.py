from email.policy import default
from enum import auto
from django.db import models
from datetime import date, datetime, timedelta
import pytz
class Event(models.Model):
    title=models.CharField(max_length=150)
    duration=models.DurationField()
    block=models.BooleanField(default=False)
    day=models.CharField(max_length=150)
    def __str__(self):
        #it will return the titlepython
        return self.title

class FinalManager(models.Manager):
    def create_Finalized(self, title, duration, st, day):
        if day == "monday":
            i = 0
        elif day == "tuesday":
            i = 1
        elif day == "wednesday":
            i = 2
        elif day == "thursday":
            i = 3
        else:
            i = 4
        today = date.today()
        day_of_week = (today - timedelta(days=(today.weekday() - i)))
        addtime = timedelta(minutes=0)
        if duration > timedelta(hours=1):
            self.create(title=title,start = datetime.combine(day_of_week, st.time(), tzinfo=pytz.UTC), end = datetime.combine(day_of_week, (st + timedelta(hours=1)).time(), tzinfo=pytz.UTC), day=day)
            self.create(title='break',start = datetime.combine(day_of_week,(st + timedelta(hours=1)).time(), tzinfo=pytz.UTC), end = datetime.combine(day_of_week, (st + timedelta(hours=1, minutes=15)).time(), tzinfo=pytz.UTC), day=day)
            nextdur = duration - timedelta(hours=1)
            addtime += timedelta(minutes=15)
            addtime += FinalManager.create_Finalized(self, title=title, duration=nextdur,st = st + timedelta(hours=1, minutes=15),day=day)
        else:
            finalized = self.create(title=title, start = datetime.combine(day_of_week, st.time(), tzinfo=pytz.UTC), end = datetime.combine(day_of_week, (st+duration).time(), tzinfo=pytz.UTC), day=day)
        return addtime

class Finalized(models.Model):
    title=models.CharField(max_length=150)
    start=models.DateTimeField()
    end=models.DateTimeField()
    day=models.CharField(max_length=150)
    objects = FinalManager()
    def __str__(self):
        #it will return the titlepython
        return self.title + self.start.strftime('%m/%d/%Y-%H:%M')


