from rest_framework import serializers
 
# import the todo data model
from .models import Event
from .models import Finalized
# create a serializer class
class EventSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Event
        fields = ('id', 'title','duration','block', 'day')
class FinalizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finalized
        fields = ('id', 'text', 'start', 'end', 'day')
