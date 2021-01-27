from django.urls import path 
from .views import hotel_information,hotel_information_create,hotel_information_edit,hotel_information_images,hotel_information_image_delete,city_information,city_information_create,city_information_edit,city_information_images,city_information_image_delete,places_information,places_information_create,places_information_edit,places_information_images,place_information_image_delete,HotelOrRestaurantsInformationLCAPIView,HotelOrRestaurantsImageLCAPIView,CityInformationLCAPIView,CityImageLCAPIView,PlacesToVisitLCAPIView,PlacesImagesLCAPIView


urlpatterns=[
	path('hotel-information/',hotel_information,name='hotel-information'),
	path('hotel-information/create/',hotel_information_create,name='hotel-information-create'),
	path('hotel-information/edit/<id>',hotel_information_edit,name='hotel-information-edit'),
	path('hotel-information/images/<id>/',hotel_information_images,name='hotel-information-images'),
	path('hotel-information/images/delete/<id>/',hotel_information_image_delete,name='hotel-information-images-delete'),
	path('city-information/',city_information,name='city-information'),
	path('city-information/create/',city_information_create,name='city-information-create'),
	path('city-information/edit/<id>/',city_information_edit,name='city-information-edit'),
	path('city-information/images/<id>/',city_information_images,name='city-information-images'),
	path('places-information/',places_information,name='places-information'),
	path('places-information/edit/<id>/',places_information_edit,name='places-information-edit'),
	path('places-information/images/<id>/',places_information_images,name='places-images'),
	path('places-information/images/delete/<id>/',place_information_image_delete,name='places-images-delete'),
	path('places-information/create/',places_information_create,name="places-information-create"),
	path('city-information/images/delete/<id>/',city_information_image_delete,name='city-information-images-delete'),
	path('hotel-information/lc/',HotelOrRestaurantsInformationLCAPIView.as_view(),name="hotel-information-lc"),
	path('hotel-restaurants-images/lc/',HotelOrRestaurantsImageLCAPIView.as_view(),name="hotel-restaurants-images-lc"),
	path('city-information/lc/',CityInformationLCAPIView.as_view(),name="city-information-lc"),
	path('city-images/lc/',CityImageLCAPIView.as_view(),name="city-images-lc"),
	path('place-to-visit/lc/',PlacesToVisitLCAPIView.as_view(),name="place-to-visit-lc"),
	path('place-image/lc/',PlacesImagesLCAPIView.as_view(),name="places-image-lc")

]