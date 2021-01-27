from django.urls import path
from .views import ServicesLCAPIView,ServiceItemCreateAPIView,ServiceItemListAPIView,ServiceItemRUDAPIView,ServicesTotalListCreateAPIView,services,service_create,service_edit


urlpatterns =	[
	path('',services,name='services'),
	path('edit/<id>/',service_edit,name='service-edit'),
	path('create/',service_create,name='service-create'),
	path('lc/',ServicesLCAPIView.as_view(),name='service lc'),
	path('service-item/create/',ServiceItemCreateAPIView.as_view(),name='service-item-create'),
	path('service-item/list/<room>/',ServiceItemListAPIView.as_view(),name='service-item-list'),
	path('service-item/rud/id/',ServiceItemRUDAPIView.as_view(),name='service-item-rud'),
	path('services-total/<room>/',ServicesTotalListCreateAPIView.as_view(),name='service-total')

]