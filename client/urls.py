from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import ClientViewSet

router = SimpleRouter()

router.register("clients", ClientViewSet)

urlpatterns = [

]
