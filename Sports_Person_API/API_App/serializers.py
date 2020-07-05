from rest_framework import serializers
from .models import Sports_person

class Sports_person_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sports_person
        fields = ('person_id', 'name', 'sport')