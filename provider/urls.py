from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import ProviderViewSet

router = SimpleRouter()

router.register("provider", ProviderViewSet)


urlpatterns = [
]