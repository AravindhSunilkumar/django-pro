from django.contrib import admin
from .models import add_profile ,vehicle_owner,Booking ,FAQ
# # Register your models here.

# admin.site.register(VehicleOwner)
admin.site.register(add_profile)
admin.site.register(vehicle_owner)
admin.site.register(Booking)
admin.site.register(FAQ)