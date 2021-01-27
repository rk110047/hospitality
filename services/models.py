from django.db import models
from django.db.models.signals import pre_save

# Create your models here.


class Service(models.Model):
	service_name		=		models.CharField(max_length=120)
	description			=		models.TextField()
	service_price 		=		models.DecimalField(default=0.00,decimal_places=2,max_digits=10)


	def __str__(self):
		return self.service_name


class ServiceItem(models.Model):
	room				=		models.CharField(max_length=120)
	service 			=		models.ForeignKey(Service,on_delete=models.CASCADE)
	price 				=		models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	active 				=		models.BooleanField(default=True)

	def __str__(self):
		return self.room

def ServiceItemPriceSignal(sender,instance,*args,**kwargs):
	instance.price 		=		instance.service.service_price


pre_save.connect(ServiceItemPriceSignal,sender=ServiceItem)

class ServicesTotal(models.Model):
	room 				=		models.CharField(max_length=120)
	service_item	 	=		models.ManyToManyField(ServiceItem,blank=True)
	total 				=		models.DecimalField(default=0.00,max_digits=10,decimal_places=2)


	def __str__(self):
		return self.room