from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'Train', views.TrainList)
# router.register(r'Wagon', views.WagonList)
# router.register(r'Privelege', views.PrivilegeList)
# router.register(r'City', views.CityList)
# router.register(r'Service', views.ServiceList)
# router.register(r'Trip', views.TripList)
# router.register(r'Ticket', views.TicketList)



urlpatterns = [
    # path('rest/', include(router.urls)),

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

# uuid:id работает с ююид; не работает с удалением 