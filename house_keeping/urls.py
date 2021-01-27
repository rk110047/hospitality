from django.urls import path
from .views import RoomServicesListCreateAPIView


urlpatterns=[
	path('room-services/lc/',RoomServicesListCreateAPIView.as_view(),name='room-services-lc')

]