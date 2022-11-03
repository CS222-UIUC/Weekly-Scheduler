from django.contrib import admin
 
# import the model Todo
from .models import Event
 
# create a class for the admin-model integration
class EventAdmin(admin.ModelAdmin):
 
    # add the fields of the model here
    list_display = ("title","duration","block", "day")
 
# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Event,EventAdmin)
