from django.shortcuts import render

from rest_framework.decorators import action


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from .models import User, Train, Wagon, Privilege, City, Service, Trip, Ticket
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, TrainSerializer, WagonSerializer, PrivilegeSerializer, CitySerializer, ServiceSerializer, TripSerializer, TicketSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class WagonViewSet(viewsets.ModelViewSet):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer


class PrivelegeViewSet(viewsets.ModelViewSet):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


