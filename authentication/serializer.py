from rest_framework  import serializers
from .models import FinalCharges



class FinalChargesSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	FinalCharges
		fields 		=	"__all__"