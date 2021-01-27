from django.urls import path
from .views import FinalChargesDetailAPIView,login_user,logout_user,index,room_detail

urlpatterns=[
	path('',index,name='index'),
	path('login/',login_user,name='login'),
	path('logout/',logout_user,name='logout'),
	path('final-total/<room>/',FinalChargesDetailAPIView.as_view(),name='final-total'),
	path('room_detail/<room>/',room_detail,name="room-detail")
]