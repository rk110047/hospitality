from django.shortcuts import render
from .serializer import TaxiBookingSerializer
from .models import TaxiBooking
from rest_framework import generics
# Create your views here.

class TaxiBookingAPIView(generics.ListCreateAPIView):
	queryset 					=	TaxiBooking.objects.all()
	authentication_classes		=	[]
	permission_classes			=	[]
	serializer_class 			=	TaxiBookingSerializer		
