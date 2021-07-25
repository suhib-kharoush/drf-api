from django.shortcuts import render
from django.db import models
from rest_framework import generics
from .models import Maintenance
from .serializer import SerializerMaintenance

# Create your views here.
class PostsListView(generics.ListCreateAPIView):
    serializer_class = SerializerMaintenance
    queryset = Maintenance.objects.all()

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerMaintenance
    queryset = Maintenance.objects.all()