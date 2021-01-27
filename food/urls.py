from django.urls import path
from .views import foodItems,foodItemCreate,food_item_edit,foodItemTmages,food_item_image_delete,FoodTypeListCreateAPIView,FoodItemListCreateAPIView,FoodImagesListCreateAPIView,FoodItemOrderListCreateAPIView,FoodItemRUDAPIView,FoodTotalListCreateAPIView


urlpatterns=[
	path('',foodItems,name='food-items'),
	path('edit/<id>/',food_item_edit,name='food-item-edit'),
	path('create/',foodItemCreate,name='food-item-create'),
	path('images/<id>/',foodItemTmages,name='food-item-images'),
	path('images/delete/<id>/',food_item_image_delete,name='food-item-image-delete'),
	path('food-type/lc/',FoodItemListCreateAPIView.as_view(),name="food-type-lc"),
	path('food-item/lc/',FoodItemListCreateAPIView.as_view(),name='food-item-lc'),
	path('food-images/lc/<id>/',FoodImagesListCreateAPIView.as_view(),name='food-images-lc'),
	path('food-item-ordered/lc/<room>/',FoodItemOrderListCreateAPIView.as_view(),name='food-item-ordered-lc'),
	path('food-item-ordered/rud/<id>/',FoodItemRUDAPIView.as_view(),name='food-item-rud'),
	path('food-total/<room>/',FoodTotalListCreateAPIView.as_view(),name='food-total')
	
]