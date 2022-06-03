from django.contrib import admin
from django.urls import include, path
# from DjandoPo.AroundTheWorld import TrainTicket
from rest_framework import routers
from TrainTicket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('TrainTicket.urls')),
    # path('train/', views.TrainList.as_view),
    # path('user/', views.UserList.as_view()),
]