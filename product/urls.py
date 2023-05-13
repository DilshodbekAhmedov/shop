from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet

router = SimpleRouter()
router.register("category", CategoryViewSet)
router.register("product", ProductViewSet)

urlpatterns = [
]