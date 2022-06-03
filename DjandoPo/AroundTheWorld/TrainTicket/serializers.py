from dataclasses import field
from rest_framework import serializers
from .models import User, Train, Wagon, Privilege, City, Service, Trip, Ticket

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

class WagonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wagon
        fields = '__all__'

class PrivilegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Privilege
        fields = '__all__'

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'