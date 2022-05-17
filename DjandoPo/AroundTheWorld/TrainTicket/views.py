from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import User, Train, Wagon, Privilege, City, Service, Trip, Ticket
from .serializers import UserSerializer, TrainSerializer, WagonSerializer, PrivilegeSerializer, CitySerializer, ServiceSerializer, TripSerializer, TicketSerializer



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TrainList(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

class TrainDetail(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class WagonList(generics.ListCreateAPIView):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer

class WagonDetail(generics.ListCreateAPIView):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer


class PrivilegeList(generics.ListCreateAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer

class PrivilegeDetail(generics.ListCreateAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetail(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetail(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

