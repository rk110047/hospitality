from django.shortcuts import render,redirect
from .serializer import FinalChargesSerializer
from .models import FinalCharges,RoomDetail
from services.models import ServicesTotal,ServiceItem
from food.models import FoodTotal,FoodItemOrders
from rest_framework import generics
from rest_framework.response import Response
from decimal import Decimal
from django.contrib.auth import get_user_model,login,logout
from django.contrib.auth import authenticate,get_user_model
# Create your views here.

User = get_user_model()

class FinalChargesDetailAPIView(generics.ListAPIView):
	queryset 				=		FinalCharges.objects.all()
	serializer_class		=		FinalChargesSerializer

	def get(self,request,room=None):
		final_charges,_ 					=	FinalCharges.objects.get_or_create(room=room)
		final_charges 						=	FinalCharges.objects.get(id=final_charges.id)
		service_charges 					=	ServicesTotal.objects.get(room=room)
		food_charges 						=	FoodTotal.objects.get(room=room)
		final_charges.service_charges 		=	service_charges.total
		final_charges.food_charges 			=	food_charges.total
		final_charges.charges 				=	Decimal(service_charges.total)+Decimal(food_charges.total)
		final_charges.save()
		serialize 				=	FinalChargesSerializer(final_charges)
		return Response(serialize.data)


def login_user(request):
	if request.method=="POST":
		username   =   request.POST['username']
		password   =   request.POST['password']
		user       =	authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("index")
		return render(request,'login.html',{})
	return render(request,'login.html',{})


def logout_user(request):
	logout(request)
	return redirect('login')

def index(request):
	if request.user.is_authenticated:
		obj =	RoomDetail.objects.all()
		return render(request,'index.html',{'obj':obj})
	return redirect('login')

def room_detail(request,room=None):
	final_charges,_ 					=	FinalCharges.objects.get_or_create(room=room)
	final_charges 						=	FinalCharges.objects.get(id=final_charges.id)
	services 							=	ServiceItem.objects.filter(room=room)
	foods 								=	FoodItemOrders.objects.filter(room=room)
	service_charges 					=	ServicesTotal.objects.get(room=room)
	food_charges 						=	FoodTotal.objects.get(room=room)
	final_charges.service_charges 		=	service_charges.total
	final_charges.food_charges 			=	food_charges.total
	final_charges.charges 				=	Decimal(service_charges.total)+Decimal(food_charges.total)
	final_charges.save()
	obj 								=   final_charges
	return render(request,'room-details.html',{'obj':obj,'services':services,'food':foods})