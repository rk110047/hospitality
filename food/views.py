from django.shortcuts import render,redirect
from rest_framework.response import Response
from .serializer import FoodTypeSerializer,FoodItemSerializer,FoodImagesSerializer,FoodItemOrdersSerializer,FoodTotalSerializer
from .models import FoodType,FoodItem,FoodImages,FoodItemOrders,FoodTotal
from rest_framework import generics
from decimal import Decimal
from .forms import FoodCreateForm,FoodItemImagesForm
from django.contrib.auth.decorators import login_required


# Create your views here.


class FoodTypeListCreateAPIView(generics.ListCreateAPIView):
	queryset				=		FoodType.objects.all()
	serializer_class 		=		FoodTypeSerializer



class FoodItemListCreateAPIView(generics.ListCreateAPIView):
	queryset				=		FoodItem.objects.all()
	serializer_class 		=		FoodItemSerializer



class FoodImagesListCreateAPIView(generics.ListCreateAPIView):
	queryset				=		FoodImages.objects.all()
	serializer_class 		=		FoodImagesSerializer



	def get(self,request,id=None):
		food_item			=		FoodItem.objects.get(id=id)
		food_images 		=		FoodImages.objects.filter(food_item=food_item)
		serialize 			=		FoodImagesSerializer(food_images,many=True)
		return Response(serialize.data)


class FoodItemOrderListCreateAPIView(generics.ListCreateAPIView):
	queryset				=		FoodItemOrders
	serializer_class		=		FoodItemOrdersSerializer


	def get(self,request,room=None):
		food_item_ordered			=		FoodItemOrders.objects.filter(room=room,active=True)
		serialize 					=		FoodItemOrdersSerializer(food_item_ordered,many=True)
		return Response(serialize.data)

class FoodItemRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset				=		FoodItemOrders
	serializer_class		=		FoodItemOrdersSerializer
	lookup_field			=		'id'


class FoodTotalListCreateAPIView(generics.ListAPIView):
	queryset				=		FoodTotal.objects.all()
	serializer_class		=		FoodTotalSerializer


	def get(self,request,room=None):
		food_total,_					=	FoodTotal.objects.get_or_create(room=room)
		food_total						=	FoodTotal.objects.get(id=food_total.id)
		food_item 						=	FoodItemOrders.objects.filter(room=room)
		print(food_item)
		if food_item.count==0:
			serialize 					=	FoodTotalSerializer(food_total,many=True)
			return Response(serialize.data)
		total 						=		0.00
		for food_item in food_item:
			food_total.food_items.add(food_item)
			total 					=		Decimal(total)+Decimal(food_item.price)
			food_total.save()
		food_total.total			=		total
		food_total.save()
		print(food_total)
		serialize 					=	FoodTotalSerializer(food_total)
		return Response(serialize.data)

@login_required(login_url='/login/')
def foodItems(request):
	foods 		=		FoodItem.objects.all()
	return render(request,'food-items.html',{'foods':foods})

@login_required(login_url='/login/')
def foodItemCreate(request):
	if request.method=="POST":
		form 	=	FoodCreateForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	form 		=	FoodCreateForm()
	return render(request,'food-item-create.html',{'form':form})


@login_required(login_url="/login/")
def food_item_edit(request,id=None):
	food_item 	=	FoodItem.objects.get(id=id)
	if request.method=="POST":
		form 	=	FoodCreateForm(request.POST,instance=food_item)
		if form.is_valid():
			form.save()
	form 		=	FoodCreateForm(instance=food_item)
	return render(request,'food-item-edit.html',{'form':form})




@login_required(login_url='/login/')
def foodItemTmages(request,id=None):
	food_item    =       FoodItem.objects.get(id=id)
	if request.method=="POST":
		food_item    =       FoodItem.objects.get(id=id)
		image   =		request.FILES['image']
		print(image)
		obj     =        FoodImages.objects.create(food_item=food_item,image=image)
		obj.save()
	data 		=		FoodImages.objects.filter(food_item=food_item)
	print(data)
	form 		=		FoodItemImagesForm()
	return render(request,'food-item-images.html',{'data':data,'form':form,'id':id})



@login_required(login_url='/login/')
def food_item_image_delete(request,id=None):
	item 	=	FoodImages.objects.get(id=id)
	id      =    item.food_item.id
	item.delete()
	return redirect(F'/food/images/{id}/')

