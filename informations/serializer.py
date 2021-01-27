from rest_framework import serializers
from .models import HotelOrRestaurantsInformation,HotelOrRestaurantsImage,CityInformation,CityImage,PlacesToVisit,PlacesImages



class HotelOrRestaurantsInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model 			=	HotelOrRestaurantsInformation
		fields 			=	"__all__"


class HotelOrRestaurantsImageSerializer(serializers.ModelSerializer):
	class Meta:
		model 			=	HotelOrRestaurantsImage
		fields 			=	"__all__"


class CityInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model 			=	CityInformation
		fields 			=	"__all__"

class CityImageSerializer(serializers.ModelSerializer):
	class Meta:
		model 			=	CityImage
		fields 			=	"__all__"


class PlacesToVisitSerializer(serializers.ModelSerializer):
	class Meta:
		model 			=	PlacesToVisit
		fields 			=	"__all__"

class PlacesImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model 			=	PlacesImages
		fields 			=	"__all__"
