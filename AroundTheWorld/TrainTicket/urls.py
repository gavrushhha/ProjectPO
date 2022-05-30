from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    # path('', views.main_trips, name='homepage'),
    # path('ticket/', views.all_ticket_item, name='ticket'),
    path('', views.index, name="index"),
    path('addtrip/',views.addTrips,name="addtrip"),
    path('loginform/',views.loginform,name="loginform"),
    path('login/',views.login,name="login"),
    path('registerform/',views.registerform,name="registerform"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('trainform/',views.trainform,name="trainform"),
    path('<train_id>',views.train_id,name="train_id"),
    path('book/',views.book,name="book"),
    path('bookform/',views.bookform,name="bookform"),
    path('mybooking/',views.mybooking,name="mybooking"),
    path('booking/<ticket_id>',views.booking,name="booking"),
    path('privileges/', views.privileges, name="privileges")

]