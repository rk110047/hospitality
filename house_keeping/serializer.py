from rest_framework import serializers
from .models import RoomServices


class RoomServicesSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		RoomServices
		fields 		=		"__all__"