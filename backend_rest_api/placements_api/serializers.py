from rest_framework import serializers 
from .models import Placement, FosterParent, FosterSibling


class PlacementSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Placement # tell django which model to use
        # THIS TELLS DJANGO WHAT DB FIELDS TO GRAB AND SEND TO THE FRONT END!!!!!(6-HOURS OF MY LIFE)
        fields = ('id', 'num', 'name', 'start_date', 'end_date', 'location', 'notes', 'time_stamp', 'user')

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FosterParent 
        fields = ('first_name', 'last_name', 'url', 'time_stamp', 'placement', 'id')

class SiblingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FosterSibling 
        fields = ('first_name', 'last_name', 'time_stamp', 'placement', 'id')
