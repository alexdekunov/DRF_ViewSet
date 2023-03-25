from rest_framework import generics, viewsets
from django.shortcuts import render
from .models import Soft
from .serializers import SoftSerializer


class SoftViewSet(viewsets.ModelViewSet):
    queryset = Soft.objects.all()
    serializer_class = SoftSerializer

# class SoftAPIView(generics.ListAPIView):
#     queryset = Soft.objects.all()
#     serializer_class = SoftSerializer
