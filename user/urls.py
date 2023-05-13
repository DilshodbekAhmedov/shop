from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserViewSet
from django.urls import path, include


router = SimpleRouter()

router.register("user", UserViewSet)

urlpatterns = [
]