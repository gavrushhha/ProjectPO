from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from TrainTicket import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    
    path('train/', views.TrainList.as_view()),
    path('train/<int:pk>/', views.TrainDetail.as_view()),
    
    path('wagon/', views.WagonList.as_view()),
    path('wagon/<int:pk>/', views.WagonDetail.as_view()),
    
    path('privilege/', views.PrivilegeList.as_view()),
    path('privilege/<int:pk>/', views.PrivilegeDetail.as_view()),   

    path('city/', views.CityList.as_view()),
    path('city/<int:pk>/', views.CityDetail.as_view()),

    path('service/', views.ServiceList.as_view()),
    path('service/<int:pk>/', views.ServiceDetail.as_view()),

    path('trip/', views.TripList.as_view()),
    path('trip/<int:pk>/', views.TripDetail.as_view()),

    path('ticket/', views.TicketList.as_view()),
    path('ticket/<int:pk>/', views.TicketDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

