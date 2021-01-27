from django.db import models

# Create your models here.


class FinalCharges(models.Model):
	room 			=		models.CharField(max_length=120)
	paid 			=		models.BooleanField(default=False)
	service_charges =		models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	food_charges  	=		models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	charges 		=		models.DecimalField(default=0.00,max_digits=10,decimal_places=2)


	def __str__(self):
		return self.room


class RoomDetail(models.Model):
	room_number 	=		models.IntegerField()
	client_name 	=		models.CharField(max_length=120)

	def __str__(self):
		return str(self.room_number)