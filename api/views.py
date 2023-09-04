from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import DetectiveSerializer
from .models import Detectives


class DetectiveViewSet(viewsets.ModelViewSet):
    queryset = Detectives.objects.all().order_by('name')
    serializer_class = DetectiveSerializer