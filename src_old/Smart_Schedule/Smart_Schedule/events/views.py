import datetime as dt
from django.shortcuts import render
from django.shortcuts import render
from datetime import date, datetime, timedelta

from django.http import JsonResponse
# import view sets from the REST framework
from rest_framework import viewsets
 
# import the EventSerializer from the serializer file
from .serializers import EventSerializer
from .serializers import FinalizedSerializer
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
class FinalizedView(viewsets.ModelViewSet):
    serializer_class = FinalizedSerializer
    queryset = Finalized.objects.all()

def sort_events(request):
    Finalized.objects.all().delete()

    mon_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    tues_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    wed_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    thurs_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    fri_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    mon = Event.objects.filter(day="monday").order_by('duration')
    for i in mon:
        Finalized.objects.create_Finalized(i.title, i.duration, mon_start, i.day)
        mon_start = mon_start + i.duration
    monday = Finalized.objects.filter(day="monday").order_by('start')

    tues = Event.objects.filter(day="tuesday").order_by('duration')
    for i in tues:
        Finalized.objects.create_Finalized(i.title, i.duration, tues_start, i.day)
        tues_start += i.duration
    tuesday = Finalized.objects.filter(day="tuesday").order_by('start')

    wed = Event.objects.filter(day="wednesday").order_by('duration')
    for i in wed:
        Finalized.objects.create_Finalized(i.title, i.duration, wed_start, i.day)
        wed_start += i.duration
    wednesday = Finalized.objects.filter(day="wednesday").order_by('-start')

    thurs = Event.objects.filter(day="thursday").order_by('duration')
    for i in thurs:
        Finalized.objects.create_Finalized(i.title, i.duration, thurs_start, i.day)
        thurs_start += i.duration
    thursday = Finalized.objects.filter(day="thursday").order_by('-start')

    fri = Event.objects.filter(day="friday").order_by('duration')
    for i in fri:
        Finalized.objects.create_Finalized(i.title, i.duration, fri_start, i.day)
        fri_start += i.duration
    friday = Finalized.objects.filter(day="friday").order_by('-start')
    return render(request, 'event_list.html', {'monday' : monday, 'tuesday' : tuesday, 'wednesday' : wednesday, 'thursday' : thursday, 'friday' : friday })

def send_events(request):
    Finalized.objects.all().delete()

    mon_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    tues_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    wed_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    thurs_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    fri_start = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    mon = Event.objects.filter(day="monday").order_by('duration')
    for i in mon:
        extra = Finalized.objects.create_Finalized(i.title, i.duration, mon_start, i.day)
        mon_start = mon_start + i.duration + extra

    tues = Event.objects.filter(day="tuesday").order_by('duration')
    for i in tues:
        Finalized.objects.create_Finalized(i.title, i.duration, tues_start, i.day)
        tues_start += i.duration

    wed = Event.objects.filter(day="wednesday").order_by('duration')
    for i in wed:
        Finalized.objects.create_Finalized(i.title, i.duration, wed_start, i.day)
        wed_start += i.duration

    thurs = Event.objects.filter(day="thursday").order_by('duration')
    for i in thurs:
        Finalized.objects.create_Finalized(i.title, i.duration, thurs_start, i.day)
        thurs_start += i.duration

    fri = Event.objects.filter(day="friday").order_by('duration')
    for i in fri:
        Finalized.objects.create_Finalized(i.title, i.duration, fri_start, i.day)
        fri_start += i.duration
    finals = Finalized.objects.values()
    flist = list(finals)
    return JsonResponse(flist, safe=False)
