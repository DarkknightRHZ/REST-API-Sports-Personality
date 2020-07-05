from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Sports_person_serializer
from .models import Sports_person

# Create your views here.

class Sports_person_view_set(viewsets.ModelViewSet):
    queryset = Sports_person.objects.all().order_by('name')
    serializer_class = Sports_person
