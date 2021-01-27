from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.response import Response
from .models import Service,ServiceItem,ServicesTotal
from .serializers import ServicesSerilaizer,ServiceItemSerializer,ServiceTotalSerializer
from decimal import Decimal
from .forms import ServiceCreateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class ServicesLCAPIView(generics.ListCreateAPIView):
	queryset				=	Service.objects.all()
	authentication_classes	=	[]
	permission_classes		=	[]
	serializer_class 		=	ServicesSerilaizer


class ServiceItemCreateAPIView(generics.CreateAPIView):
	queryset				=	ServiceItem.objects.all()
	serializer_class 		=	ServiceItemSerializer


class ServiceItemListAPIView(generics.ListAPIView):
	queryset 				=	ServiceItem.objects.all()
	serializer_class 		=	ServiceItemSerializer


	def get(self,request,room=None):
		service_item 		=	ServiceItem.objects.filter(room=room)
		serialize 			=	ServiceItemSerializer(service_item,many=True)
		return Response(serialize.data)

class ServiceItemRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset 				=	ServiceItem.objects.all()
	serializer_class 		=	ServiceItemSerializer
	lookup_field 			=	"id"


class ServicesTotalListCreateAPIView(generics.ListAPIView):
	queryset				=		ServicesTotal.objects.all()
	serializer_class		=		ServiceTotalSerializer


	def get(self,request,room=None):
		service_total,_					=	ServicesTotal.objects.get_or_create(room=room)
		service_total					=	ServicesTotal.objects.get(id=service_total.id)
		service_item 					=	ServiceItem.objects.filter(room=room)
		print(service_item)
		if service_item.count==0:
			serialize 					=	ServiceTotalSerializer(service_total,many=True)
			return Response(serialize.data)
		total 						=		0.00
		for service_item in service_item:
			service_total.service_item.add(service_item)
			total 					=		Decimal(total)+Decimal(service_item.price)
			service_total.save()
		service_total.total			=		total
		service_total.save()
		print(service_total)
		serialize 					=	ServiceTotalSerializer(service_total)
		return Response(serialize.data)


def services(request):
	if request.user.is_authenticated:
		services 	=	Service.objects.all()
		return render(request,'services.html',{'services':services})
	return redirect('login')


def service_create(request):
	if request.method=="POST":
		print(request.POST)
		form = ServiceCreateForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'service-create.html',{})


@login_required(login_url="/login/")
def service_edit(request,id=None):
	service 	=	Service.objects.get(id=id)
	if request.method=="POST":
		form 	=	ServiceCreateForm(request.POST,instance=service)
		print(form.is_valid())
		if form.is_valid():
			form.save()
	form 		=	ServiceCreateForm(instance=service)
	return render(request,'service-edit.html',{'form':form})