from rest_framework import routers
from django.urls import path
from django.urls import include
from . import views

router = routers.DefaultRouter()
router.register(r'detectives',views.DetectiveViewSet)

urlpatterns =[
    path('',include(router.urls)),
    path('api—auth/',include('rest_framework.urls' , namespace='rest_framework'))
]

