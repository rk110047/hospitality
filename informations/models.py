from django.db import models

# Create your models here.


class HotelOrRestaurantsInformation(models.Model):
	name 			=		models.CharField(max_length=120)
	description 	=		models.TextField(max_length=1000)
	city			=		models.CharField(max_length=120)


	def __str__(self):
		return self.name


class HotelOrRestaurantsImage(models.Model):
	hotelOrRestaurant 		=		models.ForeignKey(HotelOrRestaurantsInformation,on_delete=models.CASCADE)
	image 					=		models.FileField(upload_to='hotel images/')

	def __str__(self):
		return F'{self.hotelOrRestaurant}'


class CityInformation(models.Model):
	name 			=		models.CharField(max_length=120)
	description 	=		models.TextField(max_length=1000)


	def __str__(self):
		return self.name


class CityImage(models.Model):
	city 			=			models.ForeignKey(CityInformation,on_delete=models.CASCADE)
	image 			=			models.FileField(upload_to='city images/')


	def __str__(self):
		return F'{self.city}'

class PlacesToVisit(models.Model):
	name 				=		models.CharField(max_length=120)
	description 		=		models.TextField(max_length=1000)
	city				=		models.CharField(max_length=120)
	opening_timming		=		models.TimeField(null=True,blank=True)
	closing_timming 	=		models.TimeField(null=True,blank=True)


	def __str__(self):
		return self.name


class PlacesImages(models.Model):
	place  			=		models.ForeignKey(PlacesToVisit,on_delete=models.CASCADE)
	image 			=		models.FileField(upload_to='places images/')

	def __str__(self):
		return F'{self.place}'
