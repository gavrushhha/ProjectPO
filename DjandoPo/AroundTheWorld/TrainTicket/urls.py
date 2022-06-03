from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
# from django.conf.urls import url


router = routers.DefaultRouter()
# router.register(r'User',views.UserViewSet)
router.register(r'Train',views.TrainViewSet)
router.register(r'Wagon', views.WagonViewSet)
router.register(r'Privelege', views.PrivelegeViewSet)
router.register(r'City', views.CityViewSet)
router.register(r'Service', views.ServiceViewSet)
router.register(r'Trip', views.TripViewSet)
router.register(r'Ticket', views.TicketViewSet)
urlpatterns = router.urls

urlpatterns = format_suffix_patterns(urlpatterns)


urlpatterns = [
    path("api/", include(router.urls)),
    path('rest/', include(router.urls)),

    # url(r'^api/train/', include('Train.urls')),
    # path('user/', views.UserList.as_view()),
    # path('user/<int:pk>/', views.UserDetail.as_view()),
    


    # path('train/<int:pk>/', views.TrainDetail.as_view()),
    
    # path('wagon/', views.WagonList.as_view()),
    # path('wagon/<int:pk>/', views.WagonDetail.as_view()),
    
    # path('privilege/', views.PrivilegeList.as_view()),
    # path('privilege/<int:pk>/', views.PrivilegeDetail.as_view()),   

    # path('city/', views.CityList.as_view()),
    # path('city/<int:pk>/', views.CityDetail.as_view()),

    # path('service/', views.ServiceList.as_view()),
    # path('service/<int:pk>/', views.ServiceDetail.as_view()),

    # path('trip/', views.TripList.as_view()),
    # path('trip/<int:pk>/', views.TripDetail.as_view()),

    # path('ticket/', views.TicketList.as_view()),
    # path('ticket/<int:pk>/', views.TicketDetail.as_view()),
]


# uuid:id работает с ююид; не работает с удалением 