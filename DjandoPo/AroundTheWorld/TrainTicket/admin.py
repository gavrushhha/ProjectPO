from django.contrib import admin
from .models import Service_to_Ticket, Train, Wagon, Privilege, City, Ticket, Trip, User, Service, Service_to_Ticket


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass

@admin.register(Wagon)
class WagonAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Privilege)
class PrivilegeAdmin(admin.ModelAdmin):

    list_display = ('category',)
    list_filter = ('category',)
    search_fields = ('category',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
    # list_display = ('trip', 'user', 'place', 'price')
    # list_filter = ('trip', 'user', 'place', 'price')
    # search_fields = ('trip', 'user', 'place', 'price')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = ('train', 'city_departure', 'city_arrival')
    list_filter = ('train', 'city_departure', 'city_arrival')
    search_fields = ('train', 'city_departure', 'city_arrival')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityList(admin.ModelAdmin):

    list_display = ('name_city',)
    list_filter = ('name_city',)
    search_fields = ('name_city',)




