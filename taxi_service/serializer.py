from rest_framework import serializers
from .models import TaxiBooking


class TaxiBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	TaxiBooking
		fields  =	"__all__"