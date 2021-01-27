from django import forms
from .models import CityImage,PlacesImages,PlacesToVisit,PlacesImages,HotelOrRestaurantsInformation,CityInformation,HotelOrRestaurantsImage


class HotelOrRestaurantsInformationForm(forms.ModelForm):
	class Meta:
		model   =	HotelOrRestaurantsInformation
		fields 	=	"__all__"


class HotelOrRestaurantsInformationImagesForm(forms.ModelForm):
	class Meta:
		model   =	HotelOrRestaurantsImage
		fields 	=	"__all__"
		exclude =	["hotelOrRestaurant"]


class CityInformationForm(forms.ModelForm):
	class Meta:
		model 	=	CityInformation
		fields 	=	"__all__"

class CityImagesForm(forms.ModelForm):
	class Meta:
		model 	=	CityImage
		fields 	=	['image',]
		exculde =   ['city']


class PlaceToVisitForm(forms.ModelForm):
	class Meta:
		model 	=	PlacesToVisit
		fields 	=	"__all__"


class PlaceToVisitImagesForm(forms.ModelForm):
	class Meta:
		model 	=	PlacesImages
		fields 	=	"__all__"
		exclude =	['place']


class PlacesToVisitImagesForm(forms.ModelForm):
	class Meta:
		model 	=	PlacesImages
		fields 	=	['image',]
		exculde =   ['place']