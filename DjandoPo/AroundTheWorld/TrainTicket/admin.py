from django.contrib import admin
from .models import Service_to_Ticket, Train, Wagon, Privilege, City, Ticket, Trip, User, Service, Service_to_Ticket
# Register your models here.

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass

@admin.register(Wagon)
class WagonAdmin(admin.ModelAdmin):
    pass

@admin.register(Privilege)
class PrivilegeAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass





