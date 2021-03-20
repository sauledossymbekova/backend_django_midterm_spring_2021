from auth_.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='journal')

urlpatterns = [
    path('token/', obtain_jwt_token),
]
urlpatterns += router.urls
