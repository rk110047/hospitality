from django.contrib import admin
from .models import Service,ServiceItem,ServicesTotal

# Register your models here.


admin.site.register(Service)
admin.site.register(ServiceItem)
admin.site.register(ServicesTotal)