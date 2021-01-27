from django.db import models

# Create your models here.


class TaxiBooking(models.Model):
	room 				=	models.IntegerField()
	destination 		=	models.CharField(max_length=120)
	no_of_persons		=	models.IntegerField()
	booking_date 		=	models.DateField()
	booking_time		=	models.TimeField()
	mobile_number 		=	models.CharField(max_length=120)
	active 				=	models.BooleanField(default=True)

	def __str__(self):
		return self.room



