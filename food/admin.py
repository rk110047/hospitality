from django.contrib import admin
from .models import FoodType,FoodItem,FoodImages,FoodItemOrders,FoodTotal
# Register your models here.


admin.site.register(FoodItem)
admin.site.register(FoodType)
admin.site.register(FoodImages)
admin.site.register(FoodItemOrders)
admin.site.register(FoodTotal)