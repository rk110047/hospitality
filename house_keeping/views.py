from django.shortcuts import render
from .models import RoomServices
from .serializer import RoomServicesSerializer
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.



class RoomServicesListCreateAPIView(generics.ListCreateAPIView):
	queryset 			=		RoomServices.objects.all()
	serializer_class 	=		RoomServicesSerializer