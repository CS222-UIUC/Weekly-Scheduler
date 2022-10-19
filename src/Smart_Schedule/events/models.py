from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=150)
    duration=models.IntegerField()
    block=models.BooleanField(default=False)
    def __str__(self):
        #it will return the title
        return self.title
