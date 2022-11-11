import datetime as dt
from django.shortcuts import render
from django.shortcuts import render
 
# import view sets from the REST framework
from rest_framework import viewsets
 
# import the EventSerializer from the serializer file
from .serializers import EventSerializer
 
# import the Event model from the models file
from .models import Event
from .models import Finalized
from .models import FinalManager
 
# create a class for the Event model viewsets
class EventView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the EventSerializer class
    serializer_class = EventSerializer
 
    # define a variable and populate it
    # with the Event list objects
    queryset = Event.objects.all()

def sort_events(request):
    Finalized.objects.all().delete()
    mon_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    tues_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    mon = Event.objects.filter(day="monday").order_by('duration')
    for i in mon:
        Finalized.objects.create_Finalized(i.title, i.duration, mon_start, i.day)
        mon_start = mon_start + i.duration
    
    monday = Finalized.objects.filter(day="monday").order_by('-start')

    tues = Event.objects.filter(day="tuesday").order_by('duration')
    for i in tues:
        Finalized.objects.create_Finalized(i.title, i.duration, tues_start, i.day)
        tues_start += i.duration
    tuesday = Finalized.objects.filter(day="tuesday").order_by('-start')
    return render(request, 'event_list.html', {'monday' : monday, 'tuesday' : tuesday })

