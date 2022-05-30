from rest_framework import serializers

from .models import Train, Wagon, Privilege, City, Service, Trip, Person, Ticket

class TrainSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Train
        fields = ('id', 'name')


class WagonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Wagon
        fields = ('id', 'name', 'train', 'class_wagon', 'capacity')


class PrivilegeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Privilege
        fields = ('id', 'category', 'discount', 'description', 'tariff')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name_city')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'is_optional')


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'train', 'city_departure_id', 'city_arrival_id', 'way_departure', 'way_arrival', 'time_departure', 'time_arrival')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username', 'full_name', 'email', 'docs', 'password')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'trip', 'wagon', 'user', 'priv', 'price', 'availability', 'place')