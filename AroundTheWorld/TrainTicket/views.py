from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Train, Wagon, Privilege, City, Service, Trip, Ticket, Person

from dotenv import load_dotenv

load_dotenv()


def index(request):
    trips = Trip.objects.all()
    return render(request,
                  './viewTrains.html',
                  {"trips": trips})

def privileges(request):
    privileges = Privilege.objects.all()
    return render(request,
                  './privileges.html',
                  {"privileges": privileges})


def addTrips(request):
    l = Trip(train=request.GET['train'],
             city_departure=request.GET['city_departure'],
             city_arrival=request.GET['city_arrival'],
             way_departure=request.GET['way_departure'],
             way_arrival=request.GET['way_arrival'],
             time_departure=request.GET['time_departure'],
             time_arrival=request.GET['time_arrival'])
    l.save()
    return render(request, './error.html', {'msg': "Successfully Added"})


def loginform(request):
    return render(request, './login.html')


# ok
def login(request):
    u = request.POST
    user = authenticate(request, username=u['username'], password=u['password'])
    if user is not None:
        auth_login(request, user)
        context = {
            'msg': "Login Successsful"
        }
    else:
        context = {
            'msg': "Error User is not registered/invalid"
        }
    return render(request, './error.html', context)


# ok
def registerform(request):
    return render(request, './register.html')


# ok
def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    u = User.objects.create_user(username=username, email=email, password=password)
    u.save()
    context = {
        'msg': "Registeration Successsful"
    }
    return render(request, './error.html', context)


# ok
def logout(request):
    auth_logout(request)

    context = {
        'msg': "Logout Successful"
    }
    return render(request, './error.html', context)


def trainform(request):
    if request.user.is_superuser:
        return render(request, './addTrips.html')
    else:
        return render(request, './error.html', {'msg': "Not an Admin"})


def train_id(request, train_id):
    wagons = Wagon.objects.filter(train_id=train_id)
    context = {
        'wagons': wagons
    }
    return render(request, './viewWagon.html', context)


def book(request):
    try:
        if request.user.is_authenticated:
            city_departure = request.POST.get('city_departure')
            city_arrival = request.POST.get('city_arrival')
            name = request.POST.get('name')
            docs = request.POST.get('docs')
            email = request.POST.get('email')
            priv = request.POST.get('priv')
            class_wagon = request.POST.get('class_wagon')
            place = request.POST.get('place')

            trip = Trip.objects.filter(city_departure=city_departure, city_arrival=city_arrival).first()
            wagon = Wagon.objects.filter(class_wagon=class_wagon).first()
            privilege = Privilege.objects.get(category=priv)

            all_persons = Person.objects.filter(username=name)

            discount = privilege.discount
            price = 5000
            price *= discount/100

            if not all_persons:
                p = Person(username=name, docs=docs, email=email)
                p.save()
                if request.user.username == name:
                    ticket = Ticket.objects.create(trip=trip, wagon=wagon, user=p, priv=privilege, place=place, price=price)
                    ticket.save()
                    ticket_need = Ticket.objects.filter(pk=ticket.pk)
                    return render(request, './trainsavailable.html', {'ticket': ticket_need})
                else:
                    return render(request, './error.html', {'msg': "Please enter the your username"})

            user = Person.objects.get(username=name, docs=docs, email=email)
            if all_persons:
                if request.user.username == name:
                    ticket = Ticket.objects.create(trip=trip, wagon=wagon, user=user, priv=privilege, place=place, price=price)
                    ticket.save()
                    ticket_need = Ticket.objects.filter(pk=ticket.pk)
                    return render(request, './trainsavailable.html', {'ticket': ticket_need})
                else:
                    return render(request, './error.html', {'msg': "Please enter yout username"})
            else:
                return render(request, './error.html', {'msg': "Please enter the correct value"})

        else:
            return render(request, './error.html', {'msg': "Not Found"})
    except:
        return render(request, './error.html', {'msg': "Error"})


def booking(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    return render(request, './error.html', {'msg': "Booked Successfully...Price to be paid is " + str(ticket.price)})


def bookform(request):
    trip = Trip.objects.all()
    privileges = Privilege.objects.all()
    wagons = Wagon.objects.all()

    departure = [i.city_departure for i in trip]
    arrival = [i.city_arrival for i in trip]
    wagon = [i.class_wagon for i in wagons]

    departure = list(set(departure))
    arrival = list(set(arrival))
    class_wagon = list(set(wagon))
    data = {
        'departure': departure,
        'arrival': arrival,
        'class_wagon': class_wagon,
        'priv': privileges
    }
    if request.user.is_authenticated:
        return render(request, './booking.html', data)
    else:
        return render(request, './error.html', {'msg': "User not authenticated"})


def mybooking(request):
    try:
        if request.user.is_authenticated:
            person = Person.objects.get(email=request.user.email)
            ticket = Ticket.objects.filter(user_id=person)
            trip = Trip.objects.filter(pk=ticket)
            return render(request, './mybooking.html', {'ticket': ticket})
        else:
            return render(request, './error.html', {'msg': "User not authenticated"})
    except:
        return render(request, './error.html', {'msg': "Error"})
