from email.policy import default
from enum import auto
from django.db import models
from datetime import date

class Event(models.Model):
    title=models.CharField(max_length=150)
    duration=models.DurationField()
    block=models.BooleanField(default=False)
    def __str__(self):
        #it will return the title
        return self.title


