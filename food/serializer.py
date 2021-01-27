from .models import FoodType,FoodItem,FoodImages,FoodItemOrders,FoodTotal
from rest_framework import serializers 


class FoodTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		FoodType
		fields		=		"__all__"



class FoodItemSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		FoodItem
		fields		=		"__all__"


class FoodImagesSerializer(serializers.ModelSerializer):
	class Meta:	
		model 		=		FoodImages
		fields		=		"__all__"


class FoodItemOrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		FoodItemOrders
		fields		=		"__all__"


class FoodTotalSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		FoodTotal
		fields		=		"__all__"