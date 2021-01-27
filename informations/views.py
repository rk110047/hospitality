from django.shortcuts import render,redirect
from rest_framework import generics
from .models import HotelOrRestaurantsInformation,HotelOrRestaurantsImage,CityInformation,CityImage,PlacesToVisit,PlacesImages
from .serializer import HotelOrRestaurantsInformationSerializer,HotelOrRestaurantsImageSerializer,CityInformationSerializer,CityImageSerializer,PlacesToVisitSerializer,PlacesImagesSerializer
from django.contrib.auth.decorators import login_required
from .forms import CityImagesForm,PlaceToVisitForm,PlaceToVisitImagesForm,HotelOrRestaurantsInformationForm,CityInformationForm,HotelOrRestaurantsInformationImagesForm
# Create your views here.


class HotelOrRestaurantsInformationLCAPIView(generics.ListCreateAPIView):
	queryset 				=	HotelOrRestaurantsInformation.objects.all()
	serializer_class		=	HotelOrRestaurantsInformationSerializer



class HotelOrRestaurantsImageLCAPIView(generics.ListCreateAPIView):
	queryset 				=	HotelOrRestaurantsImage.objects.all()
	serializer_class 		=	HotelOrRestaurantsImageSerializer



class CityInformationLCAPIView(generics.ListCreateAPIView):
	queryset 				=	CityInformation.objects.all()
	serializer_class 		=	CityInformationSerializer



class CityImageLCAPIView(generics.ListCreateAPIView):
	queryset 				=	CityImage.objects.all()
	serializer_class 		=	CityImageSerializer


class PlacesToVisitLCAPIView(generics.ListCreateAPIView):
	queryset 				=	PlacesToVisit.objects.all()
	serializer_class 		= 	PlacesToVisitSerializer


class PlacesImagesLCAPIView(generics.ListCreateAPIView):
	queryset 				=	PlacesImages.objects.all()
	serializer_class 		=	PlacesImagesSerializer


@login_required(login_url='/login/')
def hotel_information(request):
	data 		=		HotelOrRestaurantsInformation.objects.all()
	return render(request,'hotel-information.html',{'data':data})


@login_required(login_url='/login/')
def hotel_information_create(request):
	form  		=		HotelOrRestaurantsInformationForm()
	if request.method=="POST":
		form 		=	HotelOrRestaurantsInformationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	return render(request,'hotel-information-create.html',{'form':form})


@login_required(login_url="/login/")
def hotel_information_edit(request,id=None):
	hotel 	=	HotelOrRestaurantsInformation.objects.get(id=id)
	if request.method=="POST":
		form 	=	HotelOrRestaurantsInformationForm(request.POST,instance=hotel)
		if form.is_valid():
			form.save()
	form 		=	HotelOrRestaurantsInformationForm(instance=hotel)
	return render(request,'hotel-information-edit.html',{'form':form})


@login_required(login_url='/login/')
def hotel_information_images(request,id=None):
	hotel    =       HotelOrRestaurantsInformation.objects.get(id=id)
	if request.method=="POST":
		hotel    =       HotelOrRestaurantsInformation.objects.get(id=id)
		image   =		request.FILES['image']
		print(image)
		obj     =        HotelOrRestaurantsImage.objects.create(hotelOrRestaurant=hotel,image=image)
		obj.save()
	data 		=		HotelOrRestaurantsImage.objects.filter(hotelOrRestaurant=hotel)
	print(data)
	form 		=		HotelOrRestaurantsInformationImagesForm()
	return render(request,'hotel-information-images.html',{'data':data,'form':form,'id':id})


@login_required(login_url='/login/')
def hotel_information_image_delete(request,id=None):
	item 	=	HotelOrRestaurantsImage.objects.get(id=id)
	id 		=	item.hotelOrRestaurant.id
	item.delete()
	return redirect(F'/information/hotel-information/images/{id}/')



@login_required(login_url='/login/')
def city_information(request):
	data 		=		CityInformation.objects.all()
	return render(request,'city-information.html',{'data':data})



@login_required(login_url='/login/')
def city_information_create(request):
	form  		=		CityInformationForm()
	if request.method=="POST":
		form 		=	CityInformationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	return render(request,'city-information-create.html',{'form':form})

@login_required(login_url="/login/")
def city_information_edit(request,id=None):
	city 	=	CityInformation.objects.get(id=id)
	if request.method=="POST":
		form 	=	CityInformationForm(request.POST,instance=city)
		if form.is_valid():
			form.save()
	form 		=	CityInformationForm(instance=city)
	return render(request,'city-information-edit.html',{'form':form})


@login_required(login_url='/login/')
def city_information_images(request,id=None):
	city    =       CityInformation.objects.get(id=id)
	if request.method=="POST":
		city    =       CityInformation.objects.get(id=id)
		image   =		request.FILES['image']
		print(image)
		obj     =        CityImage.objects.create(city=city,image=image)
		obj.save()
	data 		=		CityImage.objects.filter(city=city)
	print(data)
	form 		=		CityImagesForm()
	return render(request,'city-information-images.html',{'data':data,'form':form,'id':id})


@login_required(login_url='/login/')
def city_information_image_delete(request,id=None):
	item 	=	CityImage.objects.get(id=id)
	id 		=	item.city.id
	item.delete()
	return redirect(F'/information/city-information/images/{id}/')



@login_required(login_url='/login/')
def places_information(request):
	data 		=		PlacesToVisit.objects.all()
	return render(request,'places-information.html',{'data':data})


@login_required(login_url='/login/')
def places_information_create(request):
	form  		=		PlaceToVisitForm()
	if request.method=="POST":
		form 		=	PlaceToVisitForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	return render(request,'places-create.html',{'form':form})


@login_required(login_url="/login/")
def places_information_edit(request,id=None):
	place 	=	PlacesToVisit.objects.get(id=id)
	if request.method=="POST":
		form 	=	PlaceToVisitForm(request.POST,instance=place)
		if form.is_valid():
			form.save()
	form 		=	PlaceToVisitForm(instance=place)
	return render(request,'places-information-edit.html',{'form':form})


@login_required(login_url='/login/')
def places_information_images(request,id=None):
	place    =       PlacesToVisit.objects.get(id=id)
	if request.method=="POST":
		place    =       PlacesToVisit.objects.get(id=id)
		image   =		request.FILES['image']
		print(image)
		obj     =        PlacesImages.objects.create(place=place,image=image)
		obj.save()
	data 		=		PlacesImages.objects.filter(place=place)
	print(data)
	form 		=		PlaceToVisitImagesForm()
	return render(request,'places-images.html',{'data':data,'form':form,'id':id})


@login_required(login_url='/login/')
def place_information_image_delete(request,id=None):
	item 	=	PlacesImages.objects.get(id=id)
	id 		=	item.place.id
	item.delete()
	return redirect(F'/information/places-information/images/{id}/')