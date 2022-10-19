from rest_framework import serializers
 
# import the todo data model
from .models import Event
 
# create a serializer class
class EventSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Event
        fields = ('id', 'title','duration','block')