from django.contrib import admin
from .models import HotelOrRestaurantsInformation,HotelOrRestaurantsImage,CityInformation,CityImage,PlacesToVisit,PlacesImages
# Register your models here.


admin.site.register(HotelOrRestaurantsInformation)
admin.site.register(HotelOrRestaurantsImage)
admin.site.register(CityInformation)
admin.site.register(CityImage)
admin.site.register(PlacesToVisit)
admin.site.register(PlacesImages)