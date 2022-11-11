import datetime as dt
from django.shortcuts import render
from django.shortcuts import render
 
# import view sets from the REST framework
from rest_framework import viewsets
 
# import the EventSerializer from the serializer file
from .serializers import EventSerializer
 
# import the Event model from the models file
from .models import Event
 
# create a class for the Event model viewsets
class EventView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the EventSerializer class
    serializer_class = EventSerializer
 
    # define a variable and populate it
    # with the Event list objects
    queryset = Event.objects.all()

def sort_events(request):
    #mon = dt.datetime.strptime('8:00:00 AM','%I:%M:%S %p')
    monday = Event.objects.filter(day="monday").order_by('duration')
    return render(request, 'event_list.html', {'monday' : monday })

