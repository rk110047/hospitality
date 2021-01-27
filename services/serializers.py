from rest_framework import serializers
from .models import Service,ServiceItem,ServicesTotal


class ServicesSerilaizer(serializers.ModelSerializer):
	class Meta:
		model 	=	Service
		fields 	=	"__all__"


class ServiceItemSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	ServiceItem
		fields  =	"__all__"

class ServiceTotalSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	ServicesTotal
		fields 	=	"__all__"