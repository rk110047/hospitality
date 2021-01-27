from django.db import models
from django.db.models.signals import pre_save
# Create your models here.


class FoodType(models.Model):
	type_name 		=		models.CharField(max_length=120)

	def __str__(self):
		return self.type_name



class FoodItem(models.Model):
	item_type 				=		models.ForeignKey(FoodType,on_delete=models.CASCADE)
	item_name				=		models.CharField(max_length=120)
	item_description		=		models.TextField(max_length=500)
	item_image				=		models.FileField(upload_to='food item images/',null=True,blank=True)
	item_price				=		models.DecimalField(default=0.00,decimal_places=2,max_digits=10)

	def __str__(self):
		return self.item_name


class FoodImages(models.Model):
	food_item				=		models.ForeignKey(FoodItem,on_delete=models.CASCADE)
	image 					=		models.FileField(upload_to='food images/')

	def __str__(self):
		return F'{self.food_item}'

class FoodItemOrders(models.Model):
	room					=		models.CharField(max_length=120)
	active					=		models.BooleanField(default=True)
	food_item				=		models.ForeignKey(FoodItem,on_delete=models.CASCADE)
	price 					=		models.DecimalField(default=0.00,max_digits=10,decimal_places=2,null=True,blank=True)


	def __str__(self):
		return self.room

def foodItemPriceSetSignalFunction(sender,instance,*args,**kwargs):
	instance.price 			=		instance.food_item.item_price


pre_save.connect(foodItemPriceSetSignalFunction,sender=FoodItemOrders)

class FoodTotal(models.Model):
	room					=		models.CharField(max_length=120)
	food_items				=		models.ManyToManyField(FoodItemOrders,blank=True)
	total 					=		models.DecimalField(default=0.00,max_digits=10,decimal_places=2)


	def __str__(self):
		return self.room