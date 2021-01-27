from django.urls import path
from .views import TaxiBookingAPIView

urlpatterns =[
	path('lc/',TaxiBookingAPIView.as_view(),name='taxi booking lc')
]