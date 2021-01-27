from django import forms
from .models import FoodItem,FoodImages


class FoodCreateForm(forms.ModelForm):
	class Meta:
		model 	=	FoodItem
		fields 	=	["item_type","item_name","item_price","item_description","item_image",]



class FoodItemImagesForm(forms.ModelForm):
	class Meta:
		model  	=	FoodImages
		fields 	=	['image']